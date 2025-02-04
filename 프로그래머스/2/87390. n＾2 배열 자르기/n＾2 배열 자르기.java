import java.util.*;

class Solution {
    public int[] solution(int n, long left, long right) {
        ArrayList<Integer> answerList = new ArrayList<>();
        for (long i = left; i <= right; i++) {
            long row = i / n;
            long col = i % n;
            answerList.add((int)(Math.max(row, col) + 1));
        }
    
        int[] answer = new int[answerList.size()];
        for (int i = 0; i < answerList.size(); i++) {
            answer[i] = answerList.get(i);
        }
        return answer;
    }
}
