import java.util.*;

class Solution {
    public int solution(int[] d, int budget) {
        int answer = 0;
        Arrays.sort(d);
        for (int money : d){
            if (money <= budget) {
                budget -= money;
                answer ++;
            }
        }
        return answer;
    }
}