import java.util.*;
import java.io.*;

public class Main {
    static int[][] move = { {-1, 0}, {1, 0}, {0, 1}, {0, -1} };

    static int[][] map;
    static boolean[][][] visited;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        map = new int[n][m];
        visited = new boolean[k + 1][n][m];

        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < m; j++) {
                map[i][j] = line.charAt(j) - '0';
            }
        }

        ArrayDeque<MangChiman> queue = new ArrayDeque<>();
        queue.add(new MangChiman(k, 0, 0, 1));
        visited[k][0][0] = true;
        boolean found = false;

        while (!queue.isEmpty()) {
            MangChiman mangChiman = queue.poll();

            if (mangChiman.x == n - 1 && mangChiman.y == m - 1) {
                System.out.println(mangChiman.moved);
                found = true;
                break;
            }

            for (int[] d : move) {
                int nx = d[0] + mangChiman.x;
                int ny = d[1] + mangChiman.y;

                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    // 이동 가능한 경우 (벽 X)
                    if (map[nx][ny] == 0 && !visited[mangChiman.canBreak][nx][ny]) {
                        visited[mangChiman.canBreak][nx][ny] = true;
                        queue.add(new MangChiman(mangChiman.canBreak, nx, ny, mangChiman.moved + 1));
                    }

                    // 벽 부수고 이동하는 경우
                    if (map[nx][ny] == 1 && mangChiman.canBreak > 0 && !visited[mangChiman.canBreak - 1][nx][ny]) {
                        visited[mangChiman.canBreak - 1][nx][ny] = true;
                        queue.add(new MangChiman(mangChiman.canBreak - 1, nx, ny, mangChiman.moved + 1));
                    }
                }
            }
        }

        if (!found) {
            System.out.println(-1);
        }
    }
}

class MangChiman {
    int canBreak;
    int x;
    int y;
    int moved;

    MangChiman(int canBreak, int x, int y, int moved) {
        this.canBreak = canBreak;
        this.x = x;
        this.y = y;
        this.moved = moved;
    }
}