import java.io.*;

public class Main {
    static final int MOD = 1000000003;
    static int N, K;
    static int[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        K = Integer.parseInt(br.readLine());

        if (K > N / 2) {
            System.out.println(0);
            return;
        }

        dp = new int[N + 1][K + 1];

        // 1번 색을 고르지 않는 경우
        // dp[i][j] = i개의 색 중에서 j개 고르기 (인접X)
        for (int i = 0; i <= N; i++) {
            dp[i][0] = 1;     
            dp[i][1] = i;     
        }

        for (int i = 2; i <= N; i++) {
            for (int j = 2; j <= K; j++) {
                dp[i][j] = (dp[i - 1][j] + dp[i - 2][j - 1]) % MOD;
            }
        }

        // 1번 색을 고르지 않은 경우: dp[N-1][K]
        // 1번 색을 고른 경우: 2번째 색은 못 고르므로 dp[N-3][K-1] (1,3,...,N-1)
        int result = (dp[N - 1][K] + dp[N - 3][K - 1]) % MOD;
        System.out.println(result);
    }
}