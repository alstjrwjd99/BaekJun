import java.util.*;

class Solution {
    final int OFFSET = 50;

    public int solution(int temperature, int t1, int t2, int a, int b, int[] onboard) {
        int timeLen = onboard.length;
        int[][] dp = new int[timeLen][101]; // 온도 범위: -50~50 -> 인덱스 0~100
        for (int[] row : dp) Arrays.fill(row, Integer.MAX_VALUE);

        dp[0][temperature + OFFSET] = 0;

        for (int time = 1; time < timeLen; time++) {
            for (int temp = 0; temp <= 100; temp++) {
                if (dp[time - 1][temp] == Integer.MAX_VALUE) continue;

                int realTemp = temp - OFFSET;
                int cost = dp[time - 1][temp];

                // 1. 에어컨 끔 -> 온도는 실외 온도 방향으로 1도 이동
                int nextTemp = realTemp;
                if (realTemp < temperature) nextTemp++;
                else if (realTemp > temperature) nextTemp--;
                update(dp, time, nextTemp + OFFSET, cost, onboard[time], t1, t2);

                // 2. 냉방 (온도 -1)
                if (realTemp > -50)
                    update(dp, time, temp - 1, cost + a, onboard[time], t1, t2);

                // 3. 난방 (온도 +1)
                if (realTemp < 50)
                    update(dp, time, temp + 1, cost + a, onboard[time], t1, t2);

                // 4. 유지
                update(dp, time, temp, cost + b, onboard[time], t1, t2);
            }
        }

        // 마지막 시점에서 가능한 온도 중 최소 비용 구하기
        int answer = Integer.MAX_VALUE;
        for (int temp = 0; temp <= 100; temp++) {
            int realTemp = temp - OFFSET;
            if (onboard[timeLen - 1] == 1 && (realTemp < t1 || realTemp > t2)) continue;
            answer = Math.min(answer, dp[timeLen - 1][temp]);
        }

        return answer;
    }

    void update(int[][] dp, int time, int tempIndex, int cost, int onboard, int t1, int t2) {
        int realTemp = tempIndex - OFFSET;
        if (realTemp < -50 || realTemp > 50) return;

        // 탑승 중이면 반드시 t1 ~ t2 사이여야 함
        if (onboard == 1 && (realTemp < t1 || realTemp > t2)) return;

        dp[time][tempIndex] = Math.min(dp[time][tempIndex], cost);
    }
}