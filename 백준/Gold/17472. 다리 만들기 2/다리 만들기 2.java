import java.io.*;
import java.util.*;

class Main {
    static int n, m;
    static int[][] graph;
    static boolean[][] visited;
    static Map<String, Integer> bridges = new HashMap<>();
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};

    static class Point {
        int x, y;
        Point(int x, int y) { this.x = x; this.y = y; }
    }

    static class Bridge {
        int a, b, cost;
        Bridge(int a, int b, int cost) {
            this.a = a; this.b = b; this.cost = cost;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        graph = new int[n][m];
        visited = new boolean[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int group = 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (!visited[i][j] && graph[i][j] == 1) {
                    bfs(i, j, group);
                    group++;
                }
            }
        }

        for (int g = 1; g < group; g++) {
            findRoad(g);
        }

        List<Bridge> edgeList = new ArrayList<>();
        for (Map.Entry<String, Integer> entry : bridges.entrySet()) {
            String[] parts = entry.getKey().split("-");
            int a = Integer.parseInt(parts[0]);
            int b = Integer.parseInt(parts[1]);
            edgeList.add(new Bridge(a, b, entry.getValue()));
        }

        Collections.sort(edgeList, Comparator.comparingInt(b -> b.cost));
        int[] parent = new int[group];
        for (int i = 0; i < group; i++) parent[i] = i;

        int answer = 0, count = 0;
        for (Bridge b : edgeList) {
            int pa = find(parent, b.a);
            int pb = find(parent, b.b);
            if (pa != pb) {
                union(parent, pa, pb);
                answer += b.cost;
                count++;
            }
        }

        if (count == group - 2) System.out.println(answer);
        else System.out.println(-1);
    }

    static void bfs(int x, int y, int group) {
        Queue<Point> queue = new ArrayDeque<>();
        queue.add(new Point(x, y));
        visited[x][y] = true;
        graph[x][y] = group;

        while (!queue.isEmpty()) {
            Point p = queue.poll();
            for (int i = 0; i < 4; i++) {
                int nx = p.x + dx[i];
                int ny = p.y + dy[i];
                if (inRange(nx, ny) && !visited[nx][ny] && graph[nx][ny] == 1) {
                    visited[nx][ny] = true;
                    graph[nx][ny] = group;
                    queue.add(new Point(nx, ny));
                }
            }
        }
    }

    static void findRoad(int group) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (graph[i][j] == group) {
                    for (int dir = 0; dir < 4; dir++) {
                        int x = i, y = j, len = 0;
                        while (true) {
                            x += dx[dir];
                            y += dy[dir];
                            if (!inRange(x, y)) break;
                            if (graph[x][y] == group) break;
                            if (graph[x][y] == 0) len++;
                            else {
                                if (len >= 2) {
                                    int g2 = graph[x][y];
                                    String key = group < g2 ? group + "-" + g2 : g2 + "-" + group;
                                    bridges.put(key, Math.min(bridges.getOrDefault(key, Integer.MAX_VALUE), len));
                                }
                                break;
                            }
                        }
                    }
                }
            }
        }
    }

    static boolean inRange(int x, int y) {
        return x >= 0 && x < n && y >= 0 && y < m;
    }

    static int find(int[] parent, int x) {
        if (parent[x] != x) parent[x] = find(parent, parent[x]);
        return parent[x];
    }

    static void union(int[] parent, int a, int b) {
        int pa = find(parent, a);
        int pb = find(parent, b);
        if (pa < pb) parent[pb] = pa;
        else parent[pa] = pb;
    }
}