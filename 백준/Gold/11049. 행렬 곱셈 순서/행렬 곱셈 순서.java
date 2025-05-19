import java.io.*;
import java.util.*;

public class Main {
    static int[][] dp;
    static Matrix[] matrices;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int K = Integer.parseInt(br.readLine());

        matrices = new Matrix[K + 1];
        dp = new int[K + 1][K + 1];

        for (int[] row : dp) Arrays.fill(row, Integer.MAX_VALUE);

        for (int i = 1; i <= K; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int row = Integer.parseInt(st.nextToken());
            int col = Integer.parseInt(st.nextToken());
            matrices[i] = new Matrix(row, col);
            dp[i][i] = 0;
        }

        for (int len = 2; len <= K; len++) {
            for (int i = 1; i <= K - len + 1; i++) {
                int j = i + len - 1;
                for (int k = i; k < j; k++) {
                    dp[i][j] = Math.min(dp[i][j], dp[i][k] + dp[k + 1][j] + matrices[i].row * matrices[k].col * matrices[j].col);
                }
            }
        }

        System.out.println(dp[1][K]);
    }

    static class Matrix {
        int row, col;

        Matrix(int row, int col) {
            this.row = row;
            this.col = col;
        }
    }
}