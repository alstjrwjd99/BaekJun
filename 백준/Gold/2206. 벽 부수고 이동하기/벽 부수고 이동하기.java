/*
* BFS 문제
*
* 벽을 한번 부술 수 있음 -> 3차원 vistied 배열 선언 [i][j][false 이면 안부숨 , true 면 부숨]
* */
import java.io.*;
import java.util.*;

class Main {
    static int n;
    static int m;
    static int[][] map;
    static boolean[][][] visited;
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, -1, 0, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        map = new int[n][m];
        visited = new boolean[n][m][2];

        for (int i = 0; i < n; i++) {
            String input = br.readLine();
            for (int j = 0; j < m; j++) {
                map[i][j] = input.charAt(j) - '0';
            }
        }
        int answer = bfs();
        System.out.println(answer);
    }

    static int bfs() {
        Queue<int[]> queue = new ArrayDeque<>();
        // x, y, 이동 횟수, 벽 부쉈는지 여부(0=아직 안 부쉈음, 1=부쉈음)
        queue.add(new int[]{0, 0, 1, 0});
        visited[0][0][0] = true;

        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int x = cur[0];
            int y = cur[1];
            int cnt = cur[2];
            int broken = cur[3];

            if (x == n - 1 && y == m - 1) return cnt;

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    // 벽이 아닌 경우
                    if (map[nx][ny] == 0 && !visited[nx][ny][broken]) {
                        visited[nx][ny][broken] = true;
                        queue.add(new int[]{nx, ny, cnt + 1, broken});
                    }
                    // 벽이고 아직 안 부쉈으면 부수고 간다
                    else if (map[nx][ny] == 1 && broken == 0 && !visited[nx][ny][1]) {
                        visited[nx][ny][1] = true;
                        queue.add(new int[]{nx, ny, cnt + 1, 1});
                    }
                }
            }
        }
        return -1;
    }
}