class Solution {
    public int solution(int[] info, int[][] edges) {
        int n = info.length;
        boolean[] visited = new boolean[n];
        visited[0] = true;
        int answer = dfs(info, edges, 1,0, visited);
        return answer;
    }
    
    // 부모 방문 & 자식 방문하지 않은 경우에 탐색
    int dfs(int[] info,int[][] edges,int sheep, int wolf, boolean[] visited){
        if (sheep == wolf) return sheep;
        int maxSheep = sheep;
        
        for (int[] edge : edges){
            int parent = edge[0];
            int child = edge[1];
            if (visited[parent] && !visited[child]){
                visited[child] = true;
                if (info[child] == 0){
                    maxSheep = Math.max(maxSheep, dfs(info, edges, sheep + 1, wolf,visited)) ;    
                }else {
                    maxSheep = Math.max(maxSheep, dfs(info, edges, sheep, wolf + 1,visited)) ;
                }
            visited[child] = false;                 
            }

        }
        return maxSheep;
    }
}