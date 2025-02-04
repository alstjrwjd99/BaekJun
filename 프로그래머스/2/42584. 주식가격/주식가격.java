import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
        int n = prices.length;
        int[] answer = new int[n];
        Deque<int[]> stack = new ArrayDeque<>();
        
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && stack.peek()[0] > prices[i]) {
                int[] top = stack.pop();
                answer[top[1]] = i - top[1];
            }
            stack.push(new int[]{prices[i], i});
        }
        
        while (!stack.isEmpty()) {
            int[] top = stack.pop();
            answer[top[1]] = n - top[1] - 1;
        }
        
        return answer;
    }
}
