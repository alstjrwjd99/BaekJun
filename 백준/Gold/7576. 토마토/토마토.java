import java.io.*;
import java.util.*;

public class Main {
    static int m, n;
    static int[][] matrix;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    static class Coor {
        int x, y;
        Coor(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static Queue<Coor> queue = new ArrayDeque<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        matrix = new int[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                matrix[i][j] = Integer.parseInt(st.nextToken());
                if (matrix[i][j] == 1) {
                    queue.offer(new Coor(i, j));
                }
            }
        }

        bfs();

        int result = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (matrix[i][j] == 0) {
                    System.out.println(-1);
                    return;
                }
                result = Math.max(result, matrix[i][j]);
            }
        }

        System.out.println(result - 1);
    }

    static void bfs() {
        while (!queue.isEmpty()) {
            Coor cur = queue.poll();
            for (int i = 0; i < 4; i++) {
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];

                if (nx >= 0 && ny >= 0 && nx < n && ny < m && matrix[nx][ny] == 0) {
                    matrix[nx][ny] = matrix[cur.x][cur.y] + 1;
                    queue.offer(new Coor(nx, ny));
                }
            }
        }
    }
}