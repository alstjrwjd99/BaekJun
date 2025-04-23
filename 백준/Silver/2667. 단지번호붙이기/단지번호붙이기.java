/**
 * https://www.acmicpc.net/problem/2667
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

        int n = Integer.parseInt(br.readLine());
        matrix = new int[n][n];
        visited = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < n; j++) {
                matrix[i][j] = line.charAt(j) - '0';
            }
        }

        ArrayList<Integer> answer = new ArrayList<Integer>();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 1 && !visited[i][j]) {
                    int cnt = bfs(i, j);
                    answer.add(cnt);
                }
            }
        }

        answer.sort(Comparator.naturalOrder());
        System.out.println(answer.size());
        for (int i = 0; i < answer.size(); i++) {
            System.out.println(answer.get(i));
        }
    }
    static boolean inRange(int x, int y) {
        return x >= 0 && x < matrix.length && y >= 0 && y < matrix[0].length;
    }

    static int bfs(int x,int y){
        Queue<Coor> q = new ArrayDeque<>();
        q.offer(new Coor(x, y));
        visited[x][y] = true;
        int cnt = 1;

        while (!q.isEmpty()) {
            Coor c = q.poll();
            for (int i = 0; i < 4; i++) {
                int nx = c.x + dx[i];
                int ny = c.y + dy[i];
                if (inRange(nx,ny) && !visited[nx][ny] && matrix[nx][ny] == 1) {
                    visited[nx][ny] = true;
                    q.offer(new Coor(nx, ny));
                    cnt++;
                }
            }
        }
        return cnt;
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
