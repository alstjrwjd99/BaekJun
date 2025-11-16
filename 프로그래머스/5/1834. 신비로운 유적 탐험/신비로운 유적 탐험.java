import java.util.*;

class Solution {

    static List<Integer>[] children1, children2;
    static int[][] dp;

    public int solution(int n1, int[][] g1, int n2, int[][] g2) {
        // 인접 리스트(무방향)
        List<Integer>[] adj1 = new ArrayList[n1 + 1];
        List<Integer>[] adj2 = new ArrayList[n2 + 1];
        children1 = new ArrayList[n1 + 1];
        children2 = new ArrayList[n2 + 1];

        for (int i = 1; i <= n1; i++) {
            adj1[i] = new ArrayList<>();
            children1[i] = new ArrayList<>();
        }
        for (int i = 1; i <= n2; i++) {
            adj2[i] = new ArrayList<>();
            children2[i] = new ArrayList<>();
        }

        // 트리1 간선
        for (int[] e : g1) {
            int a = e[0];
            int b = e[1];
            adj1[a].add(b);
            adj1[b].add(a);
        }
        // 트리2 간선
        for (int[] e : g2) {
            int a = e[0];
            int b = e[1];
            adj2[a].add(b);
            adj2[b].add(a);
        }

        // 루트 = 1 기준으로 자식 관계 만들기
        buildChildren(1, 0, adj1, children1);
        buildChildren(1, 0, adj2, children2);

        dp = new int[n1 + 1][n2 + 1];
        for (int i = 0; i <= n1; i++) {
            Arrays.fill(dp[i], -1);
        }

        // 루트(1,1)에서 최대 공통 노드 수
        return dfs(1, 1);
    }

    // 부모-자식 방향 트리 만들기
    static void buildChildren(int cur, int parent,
                              List<Integer>[] adj,
                              List<Integer>[] children) {
        for (int next : adj[cur]) {
            if (next == parent) continue;
            children[cur].add(next);
            buildChildren(next, cur, adj, children);
        }
    }

    // dp[a][b] = 서브트리(a,b)의 최대 공통 노드 수
    static int dfs(int a, int b) {
        if (dp[a][b] != -1) return dp[a][b];

        List<Integer> ca = children1[a];
        List<Integer> cb = children2[b];

        int na = ca.size();
        int nb = cb.size();

        // 자식이 한 쪽이라도 없으면, 루트(a,b) 하나만 공통으로 취할 수 있음
        if (na == 0 || nb == 0) {
            dp[a][b] = 1;
            return 1;
        }

        // MCMF를 이용한 자식 매칭
        int V = 2 + na + nb; // S + left(na) + right(nb) + T
        int S = 0;
        int T = V - 1;
        MCMF mcmf = new MCMF(V, S, T);

        // S -> 왼쪽(트리1 자식)
        for (int i = 0; i < na; i++) {
            mcmf.addEdge(S, 1 + i, 1, 0);
        }
        // 오른쪽(트리2 자식) -> T
        for (int j = 0; j < nb; j++) {
            mcmf.addEdge(1 + na + j, T, 1, 0);
        }

        // 왼쪽-오른쪽 간선: 비용 = -dp(child1, child2)
        for (int i = 0; i < na; i++) {
            int u = ca.get(i);
            for (int j = 0; j < nb; j++) {
                int v = cb.get(j);
                int w = dfs(u, v); // 하위 서브트리 최대 공통 노드 수
                mcmf.addEdge(1 + i, 1 + na + j, 1, -w);
            }
        }

        int maxMatchWeight = mcmf.maxCostFlow(Math.min(na, nb));

        int res = 1 + maxMatchWeight; // (a,b) 자신 1개 + 자식 매칭에서 얻은 공통 노드 수
        dp[a][b] = res;
        return res;
    }

    // 최소 비용 최대 유량 (SPFA)
    static class MCMF {
        static class Edge {
            int to, cap, cost, rev;
            Edge(int to, int cap, int cost, int rev) {
                this.to = to;
                this.cap = cap;
                this.cost = cost;
                this.rev = rev;
            }
        }

        int N, S, T;
        List<Edge>[] graph;

        MCMF(int n, int s, int t) {
            this.N = n;
            this.S = s;
            this.T = t;
            graph = new ArrayList[n];
            for (int i = 0; i < n; i++) {
                graph[i] = new ArrayList<>();
            }
        }

        void addEdge(int from, int to, int cap, int cost) {
            Edge fwd = new Edge(to, cap, cost, graph[to].size());
            Edge rev = new Edge(from, 0, -cost, graph[from].size());
            graph[from].add(fwd);
            graph[to].add(rev);
        }

        // flowLimit: 최대 몇 번까지 매칭(유량) 흘릴지
        int maxCostFlow(int flowLimit) {
            final int INF = 1_000_000_000;
            int flow = 0;
            int costSum = 0;

            int[] dist = new int[N];
            int[] prevv = new int[N];
            int[] preve = new int[N];
            boolean[] inQ = new boolean[N];

            while (flow < flowLimit) {
                Arrays.fill(dist, INF);
                Arrays.fill(prevv, -1);
                Arrays.fill(preve, -1);
                Arrays.fill(inQ, false);

                Queue<Integer> q = new ArrayDeque<>();
                dist[S] = 0;
                q.add(S);
                inQ[S] = true;

                // SPFA
                while (!q.isEmpty()) {
                    int v = q.poll();
                    inQ[v] = false;
                    for (int i = 0; i < graph[v].size(); i++) {
                        Edge e = graph[v].get(i);
                        if (e.cap > 0 && dist[e.to] > dist[v] + e.cost) {
                            dist[e.to] = dist[v] + e.cost;
                            prevv[e.to] = v;
                            preve[e.to] = i;
                            if (!inQ[e.to]) {
                                inQ[e.to] = true;
                                q.add(e.to);
                            }
                        }
                    }
                }

                if (prevv[T] == -1) break;   // 더 이상 증가 경로 없음
                if (dist[T] >= 0) break;     // 더 이상 비용을 줄일 수 있는(=음수) 경로 없음

                // 이번엔 항상 1만큼 흘리면 됨 (모든 간선의 cap이 1)
                int d = 1;
                for (int v = T; v != S; v = prevv[v]) {
                    Edge e = graph[prevv[v]].get(preve[v]);
                    e.cap -= d;
                    graph[v].get(e.rev).cap += d;
                }
                costSum += dist[T]; // dist[T]는 음수
                flow += d;
            }

            // 우리는 최대 가중치 매칭을 원해서 음수 비용을 썼으니 부호 뒤집기
            return -costSum;
        }
    }
}