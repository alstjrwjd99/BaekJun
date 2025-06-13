/*
* 1. dfs 백트래킹으로 벽을 세울 곳 3군데 선정하기
* 2. bfs로 안전영역 구하기
* 3. 최대값 갱신
* */
import java.io.*;
import java.util.*;

public class Main {
    static int n, m;
    static int[][] graph;
    static int answer = 0;
    static List<Point> empty = new ArrayList<>();
    static List<Point> virus = new ArrayList<>();
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    static class Point {
        int x, y;
        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        graph = new int[n][m];
        
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
                if (graph[i][j] == 0) empty.add(new Point(i, j));
                if (graph[i][j] == 2) virus.add(new Point(i, j));
            }
        }

        combination(0, 0, new Point[3]);

        System.out.println(answer);
    }

    static void combination(int start, int depth, Point[] selected) {
        if (depth == 3) {
            simulate(selected);
            return;
        }

        for (int i = start; i < empty.size(); i++) {
            selected[depth] = empty.get(i);
            combination(i + 1, depth + 1, selected);
        }
    }

    static void simulate(Point[] walls) {
        int[][] copy = new int[n][m];
        
        for (int i = 0; i < n; i++) copy[i] = graph[i].clone();
        
        for (Point p : walls) {
            copy[p.x][p.y] = 1;
        }
        
        boolean[][] visited = new boolean[n][m];
        Queue<Point> q = new LinkedList<>();
        for (Point v : virus) {
            q.offer(v);
            visited[v.x][v.y] = true;
        }

        while (!q.isEmpty()) {
            Point p = q.poll();
            for (int d = 0; d < 4; d++) {
                int nx = p.x + dx[d];
                int ny = p.y + dy[d];
                if (inRange(nx, ny) && !visited[nx][ny] && copy[nx][ny] == 0) {
                    copy[nx][ny] = 2;
                    visited[nx][ny] = true;
                    q.offer(new Point(nx, ny));
                }
            }
        }
        
        int cnt = 0;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                if (copy[i][j] == 0) cnt++;

        answer = Math.max(answer, cnt);
    }

    static boolean inRange(int x, int y) {
        return 0 <= x && x < n && 0 <= y && y < m;
    }
}