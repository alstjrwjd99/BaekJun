import java.util.*;

class Solution {
    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        
        int[] dx = {-1, 0, 1, 0};
        int[] dy = {0, -1, 0, 1};
        
        int[] answer = new int[2];
        boolean[][] visited = new boolean[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i][j] && picture[i][j] != 0) {
                    visited[i][j] = true;
                    maxSizeOfOneArea = Math.max(maxSizeOfOneArea, bfs(i, j, m, n, picture, visited, dx, dy));
                    numberOfArea++;
                }
            }
        }

        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }
    
    public int bfs(int i, int j, int m, int n, int[][] picture, boolean[][] visited, int[] dx, int[] dy) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{i, j});
        int type = picture[i][j];
        int cnt = 1;

        while (!queue.isEmpty()) {
            int[] point = queue.poll();
            int x = point[0];
            int y = point[1];

            for (int k = 0; k < 4; k++) {
                int nx = x + dx[k];
                int ny = y + dy[k];

                if (nx >= 0 && nx < m && ny >= 0 && ny < n) {
                    if (!visited[nx][ny] && picture[nx][ny] == type) {
                        queue.add(new int[]{nx, ny});
                        visited[nx][ny] = true;
                        cnt++;
                    }
                }
            }
        }
        return cnt;
    }
}