import java.io.*;
import java.lang.reflect.Parameter;
import java.util.*;

public class Main {
    static int[][] map;
    static Direction[] moveList;
    static int N;
    static boolean cantGo = false;
    static int[] dx = {0, 1, 0, -1}; // 오른, 아래, 왼, 위
    static int[] dy = {1, 0, -1, 0};
    static  int dir = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        map = new int[N][N];

        int K = Integer.parseInt(br.readLine());
        for (int i = 0; i < K; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken()) - 1;
            int y = Integer.parseInt(st.nextToken()) - 1;
            map[x][y] = 1; // 사과는 1
        }

        int L = Integer.parseInt(br.readLine());
        moveList = new Direction[L];

        for (int i = 0; i < L; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int time = Integer.parseInt(st.nextToken());
            String dir = st.nextToken();
            moveList[i] = new Direction(time, dir);
        }

        Snake snake = new Snake();
        int time = 0;
        int pointer = 0;
        while (true){
            time++;
            snake.goStraight();

            if (cantGo) break;

            if (pointer < moveList.length && moveList[pointer].time == time) {
                if (moveList[pointer].dir.equals("D")) {
                    snake.turnRight();
                } else if (moveList[pointer].dir.equals("L")) {
                    snake.turnLeft();
                }
                pointer++;
            }
        }
        System.out.println(time);
    }

    static class Snake {
        ArrayDeque<Coordinate> queue = new ArrayDeque<>();
        Coordinate head = new Coordinate(0, 0);
        Movement move = new Movement(0,1);

        Snake() {
            queue.addLast(head);
        }

        boolean inRange(int x, int y) {
            return x >= 0 && y >= 0 && x < N && y < N;
        }
        void goStraight() {
            int nx = head.x + dx[dir];
            int ny = head.y + dy[dir];

            if (!inRange(nx, ny) || isBody(nx, ny)) {
                cantGo = true;
                return;
            }

            if (map[nx][ny] == 1) {
                map[nx][ny] = 0;
                queue.addFirst(new Coordinate(nx, ny));
            } else {
                queue.addFirst(new Coordinate(nx, ny));
                queue.pollLast();
            }

            head = new Coordinate(nx, ny);
        }

        boolean isBody(int x, int y) {
            for (Coordinate c : queue) {
                if (c.x == x && c.y == y) return true;
            }
            return false;
        }
        void turnLeft() {
            dir = (dir + 3) % 4;
        }

        void turnRight() {
            dir = (dir + 1) % 4;
        }
    }

    static class Coordinate {
        int x;
        int y;
        Coordinate(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static class Direction {
        int time;
        String dir;

        Direction(int time, String dir) {
            this.time = time;
            this.dir = dir;
        }
    }

    static class Movement{
        int dx;
        int dy;
        Movement(int dx, int dy) {
            this.dx = dx;
            this.dy = dy;
        }
    }
}