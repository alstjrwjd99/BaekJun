import java.util.*;

class Solution {
    int[] dx = {-1,0,1,0};
    int[] dy = {0,1,0,-1};
    
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        
        Queue<Robot> queue = new ArrayDeque<>();
        queue.offer(new Robot(0,0,1));
        
        boolean[][] visited = new boolean[n][m];
        visited[0][0] = true;
        
        while (!queue.isEmpty()){
            Robot r = queue.poll();
            if (r.x == n-1 && r.y == m-1){
                return r.moved;
            }
            
            for (int i =0; i< 4; i++){
                int nx = r.x + dx[i];
                int ny = r.y + dy[i];
                boolean inRange = 0<= nx && 0<= ny && n > nx && m > ny;
                if (inRange && !visited[nx][ny] && maps[nx][ny] == 1){
                    queue.offer(new Robot(nx,ny, r.moved + 1 ));
                    visited[nx][ny] = true;
                }
            }
                
        }
        
        return -1;
    }
    
    class Robot{
        int x;
        int y;
        int moved;
        Robot(int x, int y,int moved){
            this.x = x;
            this.y = y;
            this.moved = moved;
        }
    }
}