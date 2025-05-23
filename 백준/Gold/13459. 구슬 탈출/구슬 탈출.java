import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static char[][] board;
    static boolean[][][][] visited;
    static int[] dx = {-1, 1, 0, 0}; // 상하좌우
    static int[] dy = {0, 0, -1, 1};

    static class Ball {
        int rx, ry, bx, by, depth;

        Ball(int rx, int ry, int bx, int by, int depth) {
            this.rx = rx;
            this.ry = ry;
            this.bx = bx;
            this.by = by;
            this.depth = depth;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        board = new char[N][M];
        int rx = 0, ry = 0, bx = 0, by = 0;

        for (int i = 0; i < N; i++) {
            board[i] = br.readLine().toCharArray();
            for (int j = 0; j < M; j++) {
                if (board[i][j] == 'R') {
                    rx = i;
                    ry = j;
                } else if (board[i][j] == 'B') {
                    bx = i;
                    by = j;
                }
            }
        }

        visited = new boolean[N][M][N][M];
        int result = bfs(rx, ry, bx, by);
        System.out.println(result);
    }

    static int bfs(int rx, int ry, int bx, int by) {
        Queue<Ball> queue = new LinkedList<>();
        queue.offer(new Ball(rx, ry, bx, by, 0));
        visited[rx][ry][bx][by] = true;

        while (!queue.isEmpty()) {
            Ball cur = queue.poll();
            if (cur.depth >= 10) return 0;

            for (int i = 0; i < 4; i++) {
                int[] nextRed = move(cur.rx, cur.ry, dx[i], dy[i]);
                int[] nextBlue = move(cur.bx, cur.by, dx[i], dy[i]);

                if (board[nextBlue[0]][nextBlue[1]] == 'O') continue; // 파란 공 빠지면 실패
                if (board[nextRed[0]][nextRed[1]] == 'O') return 1;   // 빨간 공만 빠지면 성공

                // 같은 위치면 더 많이 움직인 쪽 한 칸 뒤로
                if (nextRed[0] == nextBlue[0] && nextRed[1] == nextBlue[1]) {
                    if (nextRed[2] > nextBlue[2]) {
                        nextRed[0] -= dx[i];
                        nextRed[1] -= dy[i];
                    } else {
                        nextBlue[0] -= dx[i];
                        nextBlue[1] -= dy[i];
                    }
                }

                if (!visited[nextRed[0]][nextRed[1]][nextBlue[0]][nextBlue[1]]) {
                    visited[nextRed[0]][nextRed[1]][nextBlue[0]][nextBlue[1]] = true;
                    queue.offer(new Ball(nextRed[0], nextRed[1], nextBlue[0], nextBlue[1], cur.depth + 1));
                }
            }
        }

        return 0;
    }

    // [x좌표, y좌표, 이동거리]
    static int[] move(int x, int y, int dx, int dy) {
        int count = 0;
        while (board[x + dx][y + dy] != '#' && board[x][y] != 'O') {
            x += dx;
            y += dy;
            count++;
        }
        return new int[]{x, y, count};
    }
}