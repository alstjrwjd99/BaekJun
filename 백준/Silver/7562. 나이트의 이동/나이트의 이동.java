/**
 * https://www.acmicpc.net/problem/7562
 */

import java.io.*;
import java.util.*;

public class Main {
    static int[] dx = {-1,-2,2,1,-1,-2,1,2};
    static int[] dy = {-2,-1,-1,-2,2,1,2,1};
    static boolean[][] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testCases = Integer.parseInt(br.readLine());
        for (int i = 0; i < testCases; i++) {
            int N = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());
            Coordinate start = new Coordinate(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()),0);
            st = new StringTokenizer(br.readLine());
            Coordinate end = new Coordinate(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()),0);
            int[][] matrix = new int[N][N];

            Queue<Coordinate> queue = new ArrayDeque<>();
            visited = new boolean[N][N];

            queue.add(start);
            visited[start.x][start.y] = true;
            while (!queue.isEmpty()) {
                Coordinate current = queue.poll();
                if (current.x == end.x && current.y == end.y) {
                    System.out.println(current.cnt);
                    break;
                }
                for (int k = 0; k < 8; k++) {
                    int nextX = current.x + dx[k];
                    int nextY = current.y + dy[k];
                    if (0<= nextX && nextX < N && 0<= nextY && nextY < N && !visited[nextX][nextY]) {
                        visited[nextX][nextY] = true;
                        queue.add(new Coordinate(nextX, nextY, current.cnt + 1));
                    }
                }
            }
        }
    }
    static class Coordinate {
        int x;
        int y;
        int cnt;
        public Coordinate(int x, int y, int cnt) {
            this.x = x;
            this.y = y;
            this.cnt = cnt;
        }
    }
}