import java.io.*;
import java.util.*;

public class Main {
    static int[] files;
    static int[] prefixSum;
    static int[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        while (T-- > 0) {
            int K = Integer.parseInt(br.readLine());
            files = new int[K + 1];
            prefixSum = new int[K + 1];
            dp = new int[K + 1][K + 1];

            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 1; i <= K; i++) {
                files[i] = Integer.parseInt(st.nextToken());
                prefixSum[i] = prefixSum[i - 1] + files[i];
            }

            for (int len = 2; len <= K; len++) {
                for (int i = 1; i <= K - len + 1; i++) {
                    int j = i + len - 1;
                    dp[i][j] = Integer.MAX_VALUE;
                    for (int k = i; k < j; k++) {
                        dp[i][j] = Math.min(dp[i][j],
                                dp[i][k] + dp[k + 1][j] + prefixSum[j] - prefixSum[i - 1]);
                    }
                }
            }

            System.out.println(dp[1][K]);
        }
    }
}