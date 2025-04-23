/**
 * https://www.acmicpc.net/problem/15686
 *
 * 1. 남길 치킨집 구하기 ( 백트래킹 )
 * 2. 각 집 별로 최단 치킨 거리 구하기
 * 3. 각 경우에 대하여 케이스 최솟값 갱신
 */

import java.io.*;
import java.util.*;

public class Main {
    static int[][] matrix;
    static boolean[][] visited;
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, -1, 0, 1};

    static int m, n;
    static ArrayList<Coor> chickenHouse;
    static int answer = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        matrix = new int[n][n];
        chickenHouse = new ArrayList<Coor>();

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                matrix[i][j] = Integer.parseInt(st.nextToken());
                if (matrix[i][j] == 2) {
                    chickenHouse.add(new Coor(i,j));
                }
            }
        }

        remainChicken(0, new ArrayList<>());
        System.out.println(answer);

    }

    static void remainChicken(int start, ArrayList<Coor> made) {
        if (made.size() == m){
            visited = new boolean[n][n];
            int sum = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (matrix[i][j] == 1) {
                        int minDist = Integer.MAX_VALUE;
                        for (Coor ch : made) {
                            int dist = Math.abs(i - ch.x) + Math.abs(j - ch.y);
                            minDist = Math.min(minDist, dist);
                        }
                        sum += minDist;
                    }
                }
            }
            answer = Math.min(answer, sum);
            return;
        }

        for (int i = start; i < chickenHouse.size(); i++) {
            made.add(chickenHouse.get(i));
            remainChicken( i + 1, made);
            made.remove(chickenHouse.get(i));
        }
    }

    static boolean inRange(int x, int y) {
        return x >= 0 && x < matrix.length && y >= 0 && y < matrix[0].length;
    }

    static int bfs(int x, int y, ArrayList<Coor> chickenHouse) {
        Queue<Coor> q = new ArrayDeque<>();
        q.offer(new Coor(x,y));
        while (!q.isEmpty()) {
            Coor c = q.poll();
            for (int i = 0; i < 4; i++) {
                int nx = c.x + dx[i];
                int ny = c.y + dy[i];
                if (inRange(nx,ny) && !visited[nx][ny]) {
                    for (int k =0 ;k<chickenHouse.size();k++) {
                        if (chickenHouse.get(k).x == nx && chickenHouse.get(k).y == ny) {
                            return Math.abs(x - chickenHouse.get(k).x) + Math.abs(y - chickenHouse.get(k).y);
                        }
                    }
                    visited[nx][ny] = true;
                    q.offer(new Coor(nx, ny));
                }
            }
        }
        return Integer.MAX_VALUE;
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
