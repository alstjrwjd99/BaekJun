import java.util.*;

class Solution {

    // 가장 긴 가짜 해밀토니안 경로 길이(정점 수)
    public int solution(int[][] t) {
        if (t == null || t.length == 0) return 1; // 정점 1개 트리

        // 노드 수 추정 (정점 라벨이 0..N-1 형태로 주어진다고 가정)
        int N = 0;
        for (int[] e : t) {
            N = Math.max(N, Math.max(e[0], e[1]) + 1);
        }

        int M = t.length;
        int E = 2 * M;

        int[] head = new int[N];
        Arrays.fill(head, -1);
        int[] to = new int[E];
        int[] next = new int[E];
        int ei = 0;

        for (int[] e : t) {
            int u = e[0], v = e[1];
            to[ei] = v; next[ei] = head[u]; head[u] = ei++;
            to[ei] = u; next[ei] = head[v]; head[v] = ei++;
        }

        int root = t[0][0];

        // parent + order(DFS 방문순) -> 역순으로 postorder 처리
        int[] parent = new int[N];
        Arrays.fill(parent, -2);
        int[] stack = new int[N];
        int sp = 0;
        int[] order = new int[N];
        int ord = 0;

        parent[root] = -1;
        stack[sp++] = root;

        while (sp > 0) {
            int u = stack[--sp];
            order[ord++] = u;

            for (int e = head[u]; e != -1; e = next[e]) {
                int v = to[e];
                if (v == parent[u]) continue;
                if (parent[v] != -2) continue;
                parent[v] = u;
                stack[sp++] = v;
            }
        }

        int[] depth = new int[N];   // "되돌아오는" 가지(직선)로 쓸 수 있는 최대 길이
        int[] spread = new int[N];  // "퍼져나가는" 경로로 쓸 수 있는 최대 길이
        int[] best2 = new int[N];   // 하위에서 spread 2개를 합칠 수 있는 최대값(예외처리용)

        int ans = 1;

        for (int idx = ord - 1; idx >= 0; idx--) {
            int u = order[idx];

            // 자식 목록을 스캔하며 top들을 뽑는다.
            int childCount = 0;
            int onlyChild = -1;

            // best2 상위 2개
            int b1 = -1, b2 = -1;
            int b1v = -1, b2v = -1;

            // spread 상위 3개 (tie: depth)
            int s1 = -1, s2 = -1, s3 = -1;

            for (int e = head[u]; e != -1; e = next[e]) {
                int v = to[e];
                if (v == parent[u]) continue;

                childCount++;
                if (onlyChild == -1) onlyChild = v;

                // top2 by best2
                int bv = best2[v];
                if (bv > b1v) {
                    b2v = b1v; b2 = b1;
                    b1v = bv;  b1 = v;
                } else if (bv > b2v) {
                    b2v = bv;  b2 = v;
                }

                // insert into top3 by (spread desc, depth desc)
                s1 = insertTop3(v, s1, s2, s3, spread, depth, 0);
                s2 = tmp2; s3 = tmp3; // 아래 helper에서 갱신
            }

            if (childCount == 0) {
                depth[u] = spread[u] = best2[u] = 1;
                continue;
            }

            // b1v는 "maxV2"에 해당(가장 큰 child best2)
            int maxChildBest2 = b1v;

            // ---- (A) best2 기준 answer 업데이트(원문 코드의 첫 sort 블럭) ----
            if (childCount == 1) {
                ans = Math.max(ans, 1 + maxChildBest2);
            } else {
                if (b2 == -1) {
                    // 이론상 childCount>=2이면 b2가 있어야 함
                    // 방어적으로만 둔다.
                    ans = Math.max(ans, 1 + maxChildBest2);
                } else if (childCount == 2) {
                    ans = Math.max(ans, 1 + depth[b2] + best2[b1]);
                    ans = Math.max(ans, 1 + depth[b1] + best2[b2]);
                } else {
                    int maxDepthExclTop2 = 0;
                    for (int e = head[u]; e != -1; e = next[e]) {
                        int v = to[e];
                        if (v == parent[u]) continue;
                        if (v == b1 || v == b2) continue;
                        maxDepthExclTop2 = Math.max(maxDepthExclTop2, depth[v]);
                    }
                    ans = Math.max(ans, 1 + Math.max(maxDepthExclTop2, depth[b2]) + best2[b1]);
                    ans = Math.max(ans, 1 + Math.max(maxDepthExclTop2, depth[b1]) + best2[b2]);
                }
            }

            // ---- (B) spread 기준 DP/answer (원문 코드의 두번째 sort 블럭) ----
            if (childCount == 1) {
                int c = onlyChild;
                depth[u] = 1 + depth[c];
                spread[u] = 1 + spread[c];
                best2[u] = Math.max(maxChildBest2 + 1, spread[c] + 1);
                ans = Math.max(ans, spread[u]);
            } else if (childCount == 2) {
                // top2 spread가 필요
                int[] top2 = top2Spread(u, parent[u], head, next, to, spread, depth);
                int a = top2[0], b = top2[1];

                ans = Math.max(ans, 1 + spread[a] + spread[b]);
                depth[u] = 1 + Math.max(depth[a], depth[b]);
                spread[u] = 1 + Math.max(depth[a] + spread[b], spread[a] + depth[b]);
                best2[u] = Math.max(maxChildBest2 + 1, spread[a] + spread[b] + 1);
            } else {
                // top3 spread 필요
                int[] top3 = top3Spread(u, parent[u], head, next, to, spread, depth);
                int a = top3[0], b = top3[1], c = top3[2];

                int maxDepthExclTop3 = 0;
                for (int e = head[u]; e != -1; e = next[e]) {
                    int v = to[e];
                    if (v == parent[u]) continue;
                    if (v == a || v == b || v == c) continue;
                    maxDepthExclTop3 = Math.max(maxDepthExclTop3, depth[v]);
                }

                ans = Math.max(ans, 1 + Math.max(maxDepthExclTop3, depth[c]) + spread[a] + spread[b]);
                ans = Math.max(ans, 1 + Math.max(maxDepthExclTop3, depth[a]) + spread[b] + spread[c]);
                ans = Math.max(ans, 1 + Math.max(maxDepthExclTop3, depth[b]) + spread[a] + spread[c]);

                depth[u] = 1 + max4(maxDepthExclTop3, depth[a], depth[b], depth[c]);

                int left = Math.max(maxDepthExclTop3, Math.max(depth[a], depth[c])) + spread[b];
                int right = Math.max(maxDepthExclTop3, Math.max(depth[b], depth[c])) + spread[a];
                spread[u] = 1 + Math.max(left, right);

                best2[u] = Math.max(maxChildBest2 + 1, spread[a] + spread[b] + 1);
            }
        }

        return ans;
    }

    // ---- helpers ----

    private static int max4(int a, int b, int c, int d) {
        return Math.max(Math.max(a, b), Math.max(c, d));
    }

    // top2 by (spread desc, depth desc)
    private static int[] top2Spread(int u, int p, int[] head, int[] next, int[] to, int[] spread, int[] depth) {
        int s1 = -1, s2 = -1;
        for (int e = head[u]; e != -1; e = next[e]) {
            int v = to[e];
            if (v == p) continue;
            if (s1 == -1 || better(v, s1, spread, depth)) {
                s2 = s1;
                s1 = v;
            } else if (s2 == -1 || better(v, s2, spread, depth)) {
                s2 = v;
            }
        }
        return new int[]{s1, s2};
    }

    // top3 by (spread desc, depth desc)
    private static int[] top3Spread(int u, int p, int[] head, int[] next, int[] to, int[] spread, int[] depth) {
        int s1 = -1, s2 = -1, s3 = -1;
        for (int e = head[u]; e != -1; e = next[e]) {
            int v = to[e];
            if (v == p) continue;
            if (s1 == -1 || better(v, s1, spread, depth)) {
                s3 = s2; s2 = s1; s1 = v;
            } else if (s2 == -1 || better(v, s2, spread, depth)) {
                s3 = s2; s2 = v;
            } else if (s3 == -1 || better(v, s3, spread, depth)) {
                s3 = v;
            }
        }
        return new int[]{s1, s2, s3};
    }

    private static boolean better(int a, int b, int[] spread, int[] depth) {
        if (spread[a] != spread[b]) return spread[a] > spread[b];
        return depth[a] > depth[b];
    }

    // 아래 3개는 위에서 사용하던 임시 삽입 로직을 제거하고, 실제 계산은 top2/top3Spread로 수행합니다.
    // (코드 간결화를 위해 남겨둔 stub; 호출되지 않음)
    private static int tmp2, tmp3;
    private static int insertTop3(int cand, int s1, int s2, int s3, int[] spread, int[] depth, int dummy) {
        return cand;
    }
}