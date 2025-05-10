import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] stair = new int[n + 1];
        int[] dp = new int[n + 1];

        for (int i = 1; i <= n; i++) {
            stair[i] = Integer.parseInt(br.readLine());
        }

        if (n == 1) {
            System.out.println(stair[1]);
            return;
        }

        dp[1] = stair[1];
        dp[2] = stair[1] + stair[2];

        for (int i = 3; i <= n; i++) {
            dp[i] = Math.max(dp[i - 3] + stair[i - 1] + stair[i], dp[i - 2] + stair[i]);
        }

        System.out.println(dp[n]);
    }
}