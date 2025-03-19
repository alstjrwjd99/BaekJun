import java.util.*;
import java.io.*;

public class Main {
    static int[][] horseMove = {
            {-1, -2}, {-1, 2}, {1, -2}, {1, 2},
            {-2, -1}, {-2, 1}, {2, -1}, {2, 1}
    };

    static int[][] move = { {-1, 0}, {1, 0}, {0, 1}, {0, -1} };

    static int[][] map;
    static boolean[][][] visited;  // [남은 말 이동 횟수][x][y]로 방문 관리

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int k = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int w = Integer.parseInt(st.nextToken());
        int h = Integer.parseInt(st.nextToken());

        map = new int[h][w];
        visited = new boolean[k + 1][h][w];

        for (int i = 0; i < h; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < w; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        ArrayDeque<Monkey> queue = new ArrayDeque<>();
        queue.add(new Monkey(k, 0, 0, 0));
        visited[k][0][0] = true;
        boolean found = false;

        while (!queue.isEmpty()) {
            Monkey monkey = queue.poll();

            if (monkey.x == h - 1 && monkey.y == w - 1) {
                System.out.println(monkey.moved);
                found = true;
                break;
            }

            // 말 이동 처리
            if (monkey.moveLikeHorse > 0) {
                for (int[] d : horseMove) {
                    int nx = d[0] + monkey.x;
                    int ny = d[1] + monkey.y;

                    if (0 <= nx && nx < h && 0 <= ny && ny < w && map[nx][ny] == 0) {
                        if (!visited[monkey.moveLikeHorse - 1][nx][ny]) {
                            visited[monkey.moveLikeHorse - 1][nx][ny] = true;
                            queue.add(new Monkey(monkey.moveLikeHorse - 1, nx, ny, monkey.moved + 1));
                        }
                    }
                }
            }

            // 일반 이동 처리
            for (int[] d : move) {
                int nx = d[0] + monkey.x;
                int ny = d[1] + monkey.y;

                if (0 <= nx && nx < h && 0 <= ny && ny < w && map[nx][ny] == 0) {
                    if (!visited[monkey.moveLikeHorse][nx][ny]) {
                        visited[monkey.moveLikeHorse][nx][ny] = true;
                        queue.add(new Monkey(monkey.moveLikeHorse, nx, ny, monkey.moved + 1));
                    }
                }
            }
        }

        if (!found) {
            System.out.println(-1);
        }
    }
}

class Monkey {
    int moveLikeHorse;
    int x;
    int y;
    int moved;

    Monkey(int moveLikeHorse, int x, int y, int moved) {
        this.moveLikeHorse = moveLikeHorse;
        this.x = x;
        this.y = y;
        this.moved = moved;
    }
}