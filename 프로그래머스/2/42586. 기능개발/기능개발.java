/*
1. 시작일 기준으로 각각의 작업들이 얼마나 걸렸는지 계산
2. 앞의 작업보다 뒤에 작업이 빨리 끝난 경우 앞의 작업 갯수 + 1 해서 답에 추가
*/
import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        int n = progresses.length;
        int[] leftDays = new int[n];

        for (int i = 0; i < n; i++) {
            leftDays[i] = (int) Math.ceil((double)(100 - progresses[i]) / speeds[i]);
        }

        int baseDay = leftDays[0];
        int count = 1;

        for (int i = 1; i < n; i++) {
            if (leftDays[i] <= baseDay) {
                count++;
            } else {
                answer.add(count);
                baseDay = leftDays[i];
                count = 1;
            }
        }

        answer.add(count); 
        return answer.stream().mapToInt(i -> i).toArray();
    }
}