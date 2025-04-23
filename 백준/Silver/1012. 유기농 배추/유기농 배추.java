/**
 * https://www.acmicpc.net/problem/2178
 */

import java.io.*;
import java.util.*;

public class Main {
    static int[][] matrix;
    static boolean[][] visited;
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, -1, 0, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testcases = Integer.parseInt(br.readLine());
        for(int test = 0; test < testcases; test++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());

            matrix = new int[n][m];
            visited = new boolean[n][m];

            for(int i = 0; i < k; i++) {
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                matrix[x][y] = 1;
            }

            int answer = 0;

            for(int i = 0; i < n; i++) {
                for(int j = 0; j < m; j++) {
                    if(matrix[i][j] == 1 && !visited[i][j]) {
                        bfs(i, j);
                        answer++;
                    }
                }
            }

            System.out.println(answer);
        }

    }

    static boolean inRange(int x, int y) {
        return x >= 0 && x < matrix.length && y >= 0 && y < matrix[0].length;
    }

    static void bfs(int x,int y){
        Queue<Coor> q = new ArrayDeque<>();
        q.offer(new Coor(x, y));
        visited[x][y] = true;

        while (!q.isEmpty()) {
            Coor c = q.poll();
            for (int i = 0; i < 4; i++) {
                int nx = c.x + dx[i];
                int ny = c.y + dy[i];
                if (inRange(nx,ny) && !visited[nx][ny] && matrix[nx][ny] == 1) {
                    visited[nx][ny] = true;
                    q.offer(new Coor(nx, ny));
                }
            }
        }
    }

    static class Coor{
        int x;
        int y;
        Coor(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
