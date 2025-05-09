/*
bfs
좌표 2개짜리 움직이는 로봇
시작 : 0,0 , 0,1 오른쪽 -> 0,1 , 0,2

90도 회전 가능
0,0 일때 1,0에 뭐가 있으면 안됨 -> 0,1, 1,1

큐에 전진 , 회전 둘다 넣음
*/
import java.util.*;

class Solution {
    int[][] map;
    int n;
    int[][] dir = {{0,1},{1,0},{-1,0},{0,-1}};

    public int solution(int[][] board) {
        n = board.length;
        map = board;
        return bfs();
    }

    int bfs(){
        int cnt = 0;
        Queue<Robot> queue = new ArrayDeque<>();
        queue.offer(new Robot(0,0,0,1,0));

        Set<Robot> visited = new HashSet<>();

        while (!queue.isEmpty()){
            Robot r = queue.poll();
            if ((r.x1 == n-1 && r.y1 == n-1) || (r.x2 == n-1 && r.y2 == n-1)){
                return r.moved;
            }

            // 직진
            for(int[] d : dir){
                int nx1 = r.x1 + d[0];
                int ny1 = r.y1 + d[1];
                int nx2 = r.x2 + d[0];
                int ny2 = r.y2 + d[1];
                boolean canMove = (inRange(nx1,ny1) && inRange(nx2,ny2));
                if (canMove && map[nx1][ny1] == 0 && map[nx2][ny2] == 0 && !visited.contains(new Robot(nx1,ny1,nx2,ny2,r.moved))){
                    queue.offer(new Robot(nx1,ny1,nx2,ny2,r.moved + 1));
                    visited.add(new Robot(nx1,ny1,nx2,ny2,r.moved + 1));
                }
            }

            // 회전 가로 -> 세로
            if (r.x1 == r.x2) {
                for (int d = -1; d <= 1; d += 2) {
                    int nx1 = r.x1 + d;
                    int ny1 = r.y1;
                    int nx2 = r.x2 + d;
                    int ny2 = r.y2;
                    if (inRange(nx1, ny1) && inRange(nx2, ny2) && map[nx1][ny1] == 0 && map[nx2][ny2] == 0) {
                        Robot next1 = new Robot(r.x1, r.y1, r.x1 + d, r.y1, r.moved + 1);
                        Robot next2 = new Robot(r.x2, r.y2, r.x2 + d, r.y2, r.moved + 1);

                        if (!visited.contains(next1)) {
                            queue.offer(next1);
                            visited.add(next1);
                        }
                        if (!visited.contains(next2)) {
                            queue.offer(next2);
                            visited.add(next2);
                        }
                    }
                }
            } else if (r.y1 == r.y2) { 
                for (int d = -1; d <= 1; d += 2) { 
                    int nx1 = r.x1;
                    int ny1 = r.y1 + d;
                    int nx2 = r.x2;
                    int ny2 = r.y2 + d;

                    if (inRange(nx1, ny1) && inRange(nx2, ny2) && map[nx1][ny1] == 0 && map[nx2][ny2] == 0) {
                        Robot next1 = new Robot(r.x1, r.y1, r.x1, r.y1 + d, r.moved + 1);
                        Robot next2 = new Robot(r.x2, r.y2, r.x2, r.y2 + d, r.moved + 1);

                        if (!visited.contains(next1)) {
                            queue.offer(next1);
                            visited.add(next1);
                        }
                        if (!visited.contains(next2)) {
                            queue.offer(next2);
                            visited.add(next2);
                        }
                    }
                }
            }
        }
        return cnt;
    }

    boolean inRange (int x,int y){
        return (0<= x && 0<= y && x < n && y< n);
    }

    class Robot{
        int x1;
        int x2;
        int y1;
        int y2;
        int moved;

        Robot(int x1,int y1,int x2,int y2,int moved){
            this.x1 = x1;
            this.y1 = y1;
            this.x2 = x2;
            this.y2 = y2;
            this.moved = moved;
        }
        @Override
        public boolean equals(Object obj) {
            if (!(obj instanceof Robot)) return false;
            Robot r = (Robot) obj;
            return ((x1 == r.x1 && y1 == r.y1 && x2 == r.x2 && y2 == r.y2) || (x1 == r.x2 && y1 == r.y2 && x2 == r.x1 && y2 == r.y1));
        }

        @Override
        public int hashCode() {
            return Objects.hash(Math.min(x1, x2), Math.min(y1, y2), Math.max(x1, x2), Math.max(y1, y2));
        }
    }
}