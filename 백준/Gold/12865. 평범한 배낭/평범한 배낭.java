import java.util.*;
import java.io.*;

class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int[][] dp = new int[n + 1][k + 1];
        Product[] products = new Product[n + 1];

        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            products[i] = new Product(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= k; j++) {
                Product p = products[i];
                if (p.weight > j ){
                    dp[i][j] = dp[i - 1][j];
                }
                else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i - 1][j-p.weight] + p.price);
                }
            }
        }

        System.out.println(dp[n][k]);

    }

    static class Product {
        int weight;
        int price;
        public Product(int weight, int price) {
            this.weight = weight;
            this.price = price;
        }
    }
}