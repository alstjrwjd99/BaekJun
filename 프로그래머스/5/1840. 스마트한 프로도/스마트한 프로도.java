import java.util.*;

class Solution {

    static class Comp {
        int buffer;   // 0 / 1 / 2  (필요한 최소 하강 폭)
        int delta;    // net change = (#add) - (#del)
        boolean cycle;

        // path형으로 실행할 때 사용할 간선 순서(끝~끝)
        int[] pathEdges;

        // cycle인 경우: 먼저 삭제할 cutEdge (M0-only)
        int cutEdge;
    }

    static class IntArray {
        int[] a = new int[8];
        int sz = 0;
        void add(int v) {
            if (sz == a.length) a = Arrays.copyOf(a, a.length * 2);
            a[sz++] = v;
        }
        int size() { return sz; }
        int[] toArray() { return Arrays.copyOf(a, sz); }
    }

    // e의 다른 끝 정점
    static int other(int[] A, int[] B, int e, int v) {
        int u = A[e - 1], w = B[e - 1];
        return (v == u) ? w : u;
    }

    // v에 incident한 H-edge 중 prevE도 아니고 forbidE도 아닌 것
    static int nextEdgeSkip(int[] e1, int[] e2, int v, int prevE, int forbidE) {
        int x = e1[v];
        if (x != 0 && x != prevE && x != forbidE) return x;
        int y = e2[v];
        if (y != 0 && y != prevE && y != forbidE) return y;
        return 0;
    }

    // endpoint(startV)부터 H-edge를 따라 path 간선 순서를 만든다 (forbidEdge는 절대 포함 안 함)
    static int[] buildPath(int[] A, int[] B, int[] e1, int[] e2, int startV, int forbidEdge) {
        int curV = startV;
        int prevE = 0;
        IntArray list = new IntArray();
        while (true) {
            int e = nextEdgeSkip(e1, e2, curV, prevE, forbidEdge);
            if (e == 0) break;
            list.add(e);
            int nxtV = other(A, B, e, curV);
            prevE = e;
            curV = nxtV;
        }
        return list.toArray();
    }

    // 경로 edges가 "Mt-only(1)"로 시작하도록 필요 시 reverse
    static void reverse(int[] arr) {
        for (int i = 0, j = arr.length - 1; i < j; i++, j--) {
            int t = arr[i]; arr[i] = arr[j]; arr[j] = t;
        }
    }

    // start가 Mt-only(1)인 경로에 대해, 매칭 유지 토글 시퀀스 생성:
    // (del edges[1], add edges[0]), (del edges[3], add edges[2]) ... 마지막이 Mt-only면 마지막 add
    static void applyStartMtPath(int[] edges, byte[] type, ArrayList<int[]> ops, int[] curSizeRef) {
        int L = edges.length;
        if (L == 0) return;

        // L==1이면 add만
        if (L == 1) {
            ops.add(new int[]{1, edges[0]});
            curSizeRef[0]++;
            return;
        }

        // pairs
        for (int i = 1; i < L; i += 2) {
            // edges[i]는 M0-only(0)이어야 한다
            ops.add(new int[]{0, edges[i]});
            curSizeRef[0]--;

            ops.add(new int[]{1, edges[i - 1]});
            curSizeRef[0]++;
        }

        // 마지막이 Mt-only면 마지막 add
        if ((L % 2) == 1) {
            ops.add(new int[]{1, edges[L - 1]});
            curSizeRef[0]++;
        }
    }

    // 컴포넌트(path/cycle)를 실제 연산으로 풀어 ops에 추가
    static void emitOps(Comp c, byte[] type, ArrayList<int[]> ops, int[] curSizeRef) {
        if (!c.cycle) {
            int[] edges = c.pathEdges;

            if (edges.length == 1) {
                if (type[edges[0]] == 1) { // singleton Mt-only
                    ops.add(new int[]{1, edges[0]});
                    curSizeRef[0]++;
                } else { // singleton M0-only
                    ops.add(new int[]{0, edges[0]});
                    curSizeRef[0]--;
                }
                return;
            }

            // path 길이>=2
            int first = edges[0];
            int last = edges[edges.length - 1];

            if (type[first] == 1) {
                // 시작이 Mt-only면 그대로
                applyStartMtPath(edges, type, ops, curSizeRef);
            } else if (type[last] == 1) {
                // 반대 끝이 Mt-only면 뒤집어서 시작을 Mt-only로
                reverse(edges);
                applyStartMtPath(edges, type, ops, curSizeRef);
            } else {
                // 양끝이 모두 M0-only(case4): 끝 하나 삭제 후, 남은 경로는 Mt-only로 시작
                ops.add(new int[]{0, edges[0]});
                curSizeRef[0]--;

                int[] sub = Arrays.copyOfRange(edges, 1, edges.length);
                // sub[0]은 Mt-only가 된다
                applyStartMtPath(sub, type, ops, curSizeRef);
            }
        } else {
            // cycle: cutEdge(M0-only) 먼저 삭제 → 남은 pathEdges는 Mt-only로 시작하도록 구성해둠
            ops.add(new int[]{0, c.cutEdge});
            curSizeRef[0]--;

            applyStartMtPath(c.pathEdges, type, ops, curSizeRef);
        }
    }

    public int[][] solution(int n, int m,
                            int[] a, int[] b,
                            int k,
                            int m1, int m2,
                            int[] e1Arr, int[] e2Arr) {

        // M0, Mt 표시
        boolean[] inM0 = new boolean[m + 1];
        boolean[] inMt = new boolean[m + 1];
        for (int e : e1Arr) inM0[e] = true;
        for (int e : e2Arr) inMt[e] = true;

        // type[e] : -1 not in H, 0 = M0-only(delete), 1 = Mt-only(add)
        byte[] type = new byte[m + 1];
        Arrays.fill(type, (byte) -1);

        // H에서 각 정점 incident edge 최대 2개
        int[] ve1 = new int[n + 1];
        int[] ve2 = new int[n + 1];
        int[] deg = new int[n + 1];

        // H 간선 목록 (<= m1+m2)
        int[] diff = new int[m1 + m2 + 5];
        int diffCnt = 0;

        for (int e = 1; e <= m; e++) {
            if (!(inM0[e] ^ inMt[e])) continue;
            type[e] = (byte) (inMt[e] ? 1 : 0);
            diff[diffCnt++] = e;

            int u = a[e - 1], v = b[e - 1];
            if (ve1[u] == 0) ve1[u] = e; else ve2[u] = e;
            if (ve1[v] == 0) ve1[v] = e; else ve2[v] = e;
            deg[u]++; deg[v]++;
        }

        boolean[] seen = new boolean[m + 1];
        ArrayList<Comp> comps = new ArrayList<>();

        // 컴포넌트 추출
        for (int i = 0; i < diffCnt; i++) {
            int seed = diff[i];
            if (seen[seed]) continue;

            // 1) 이 컴포넌트의 간선들을 모으면서 endpoint(deg==1) 존재 여부 확인
            ArrayDeque<Integer> st = new ArrayDeque<>();
            st.push(seed);

            IntArray edgesInComp = new IntArray();
            int endpointV = 0;

            while (!st.isEmpty()) {
                int e = st.pop();
                if (seen[e]) continue;
                seen[e] = true;
                edgesInComp.add(e);

                int u = a[e - 1], v = b[e - 1];
                if (endpointV == 0) {
                    if (deg[u] == 1) endpointV = u;
                    else if (deg[v] == 1) endpointV = v;
                }

                int nu = nextEdgeSkip(ve1, ve2, u, e, 0);
                if (nu != 0 && !seen[nu]) st.push(nu);

                int nv = nextEdgeSkip(ve1, ve2, v, e, 0);
                if (nv != 0 && !seen[nv]) st.push(nv);
            }

            int compSize = edgesInComp.size();
            Comp c = new Comp();

            if (endpointV != 0) {
                // PATH 컴포넌트
                c.cycle = false;

                // endpointV에서 순서대로 path 만들기
                int[] ordered = buildPath(a, b, ve1, ve2, endpointV, 0);
                c.pathEdges = ordered;

                // add/del count로 delta 계산
                int add = 0, del = 0;
                for (int e : ordered) {
                    if (type[e] == 1) add++; else del++;
                }
                c.delta = add - del;

                // buffer 계산
                if (ordered.length == 1) {
                    c.buffer = (type[ordered[0]] == 1) ? 0 : 1;
                } else {
                    int first = ordered[0];
                    int last = ordered[ordered.length - 1];
                    if (type[first] == 0 && type[last] == 0) {
                        // case4는 시작부에서 연속 2삭제가 필요할 수 있음
                        c.buffer = 2;
                    } else {
                        c.buffer = 1;
                    }
                }

            } else {
                // CYCLE 컴포넌트
                c.cycle = true;
                c.delta = 0;
                c.buffer = 2;

                // cycle 순서 만들기: 한 정점에서 시작해 다시 돌아올 때까지
                int startV = a[seed - 1];
                int curV = startV;
                int prevE = 0;

                IntArray cyc = new IntArray();
                while (true) {
                    int e = nextEdgeSkip(ve1, ve2, curV, prevE, 0);
                    cyc.add(e);
                    int nxtV = other(a, b, e, curV);
                    prevE = e;
                    curV = nxtV;
                    if (curV == startV) break;
                }
                int[] cycEdges = cyc.toArray();
                int L = cycEdges.length;

                // cutEdge: M0-only(0) 하나 선택
                int cutIdx = -1;
                for (int t = 0; t < L; t++) {
                    if (type[cycEdges[t]] == 0) { cutIdx = t; break; }
                }
                int cutEdge = cycEdges[cutIdx];
                c.cutEdge = cutEdge;

                // cutEdge를 제거한 pathEdges 구성: (cutIdx+1)부터 (cutIdx-1)까지
                IntArray path = new IntArray();
                for (int t = 1; t < L; t++) {
                    int e = cycEdges[(cutIdx + t) % L];
                    path.add(e);
                }
                c.pathEdges = path.toArray(); // 양 끝이 Mt-only, 시작도 Mt-only가 되도록 구성됨
            }

            comps.add(c);
        }

        // 스케줄링: 현재 크기(curSize)에 따라 실행 가능한 컴포넌트 중 우선순위 선택
        // 우선순위: delta 큰 것 우선(슬랙 확보), buffer 작은 것 우선
        PriorityQueue<Comp> pq0 = new PriorityQueue<>((x, y) -> y.delta - x.delta);
        PriorityQueue<Comp> pq1 = new PriorityQueue<>((x, y) -> {
            if (y.delta != x.delta) return y.delta - x.delta;
            return x.buffer - y.buffer;
        });
        PriorityQueue<Comp> pq2 = new PriorityQueue<>((x, y) -> {
            if (y.delta != x.delta) return y.delta - x.delta;
            return x.buffer - y.buffer;
        });

        for (Comp c : comps) {
            if (c.buffer == 0) pq0.add(c);
            else if (c.buffer == 1) pq1.add(c);
            else pq2.add(c);
        }

        int[] curSizeRef = new int[]{m1};
        ArrayList<int[]> ops = new ArrayList<>();

        while (!pq0.isEmpty() || !pq1.isEmpty() || !pq2.isEmpty()) {
            int s = curSizeRef[0];

            Comp pick = null;

            // 실행 가능 조건:
            // buffer0: 항상 가능
            // buffer1: s >= k-1
            // buffer2: s >= k
            if (s <= k - 2) {
                // 이 상황은 정상 스케줄이면 거의 나오지 않음. 나오면 buffer0만 가능
                if (!pq0.isEmpty()) pick = pq0.poll();
                else break;
            } else if (s == k - 1) {
                // buffer2 불가
                if (!pq1.isEmpty()) pick = pq1.poll();
                else if (!pq0.isEmpty()) pick = pq0.poll();
                else break;
            } else { // s >= k
                // 세 PQ 중 "delta 큰 것" 우선으로 선택
                Comp c0 = pq0.peek();
                Comp c1 = pq1.peek();
                Comp c2 = pq2.peek();

                pick = c2; // 임시
                if (pick == null) pick = c1;
                if (pick == null) pick = c0;

                // delta 비교
                if (c1 != null && (pick == null || c1.delta > pick.delta)) pick = c1;
                if (c0 != null && (pick == null || c0.delta > pick.delta)) pick = c0;

                // 실제 pop
                if (pick == null) break;
                if (pick.buffer == 0) pq0.poll();
                else if (pick.buffer == 1) pq1.poll();
                else pq2.poll();
            }

            // 연산 출력
            emitOps(pick, type, ops, curSizeRef);

            // 안전장치(정상 입력이면 스케줄링으로 유지되어야 함)
            if (curSizeRef[0] < k - 2) {
                // 불가능한 스케줄이 발생한 경우: 즉시 실패 출력
                return new int[0][0];
            }
        }

        int[][] ans = new int[ops.size()][2];
        for (int i = 0; i < ops.size(); i++) ans[i] = ops.get(i);
        return ans;
    }
}