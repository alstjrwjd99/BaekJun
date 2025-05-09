import java.io.*;
import java.util.*;

class Main{
    static int[][] map;
    static int n;
    static int[][] directions = {{1,0},{-1,0},{0,1},{0,-1}};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int fuel = Integer.parseInt(st.nextToken());
        map = new int[n][n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        st = new StringTokenizer(br.readLine());
        int sX = Integer.parseInt(st.nextToken()) -1;
        int sY = Integer.parseInt(st.nextToken()) -1;

        Car car = new Car(sX,sY,fuel);

        for(int i = 0; i < m; i++){
            st = new StringTokenizer(br.readLine());
            int startX = Integer.parseInt(st.nextToken()) -1;
            int startY = Integer.parseInt(st.nextToken()) -1;
            int endX = Integer.parseInt(st.nextToken()) -1;
            int endY = Integer.parseInt(st.nextToken()) -1;
            car.customers.add(new Customer(startX,startY,endX,endY));
        }


        while (!car.customers.isEmpty()) {
            int minDistance = Integer.MAX_VALUE;
            Customer target = null;

            for (Customer c : car.customers) {
                int dist = car.getDistance(car.x, car.y, c.startX, c.startY);
                if (dist == -1) continue;

                if (dist < minDistance || (dist == minDistance && (c.startX < target.startX || (c.startX == target.startX && c.startY < target.startY)))) {
                    minDistance = dist;
                    target = c;
                }
            }

            if (target == null || car.fuel < minDistance) {
                car.fuel = -1;
                break;
            }

            car.fuel -= minDistance;
            int moved = car.getDistance(target.startX, target.startY, target.endX, target.endY);
            if (moved == -1 || car.fuel < moved) {
                car.fuel = -1;
                break;
            }

            car.fuel -= moved;
            car.fuel += moved * 2;
            car.x = target.endX;
            car.y = target.endY;
            car.customers.remove(target);
        }
        System.out.println(car.fuel);
    }


    static class Car {
        int x;
        int y;
        int fuel;
        List<Customer> customers = new ArrayList<>();
        public Car(int x, int y, int fuel) {
            this.x = x;
            this.y = y;
            this.fuel = fuel;
        }

        @Override
        public String toString() {
            return "x, y -> " + x + "," + y + ", fuel : " + fuel;
        }

        int getDistance(int x1, int y1, int x2, int y2) {
            Queue<int[]> queue = new ArrayDeque<>();
            queue.add(new int[]{x1, y1, 0});
            boolean[][] visited = new boolean[n][n];
            visited[x1][y1] = true;

            while (!queue.isEmpty()) {
                int[] cur = queue.poll();
                if (cur[2] > fuel) {
                    return -1;
                }
                if (cur[0] == x2 && cur[1] == y2) {
                    return cur[2];
                }
                for (int[] direction : directions) {
                    int nx = cur[0] + direction[0];
                    int ny = cur[1] + direction[1];
                    boolean inRange = (0<= nx && nx < n && 0<= ny && ny < n);
                    if (inRange && !visited[nx][ny] && map[nx][ny] == 0) {
                        queue.add(new int[]{nx, ny, cur[2] + 1});
                        visited[nx][ny] = true;
                    }
                }
            }
            return -1;
        }
    }


    static class Customer {
        int startX;
        int startY;
        int endX;
        int endY;
        Customer(int startX, int startY, int endX, int endY) {
            this.startX = startX;
            this.startY = startY;
            this.endX = endX;
            this.endY = endY;
        }

        @Override
        public String toString() {
            return "Customer{" +
                    "startX=" + startX +
                    ", startY=" + startY +
                    ", endX=" + endX +
                    ", endY=" + endY +
                    '}';
        }
    }
}