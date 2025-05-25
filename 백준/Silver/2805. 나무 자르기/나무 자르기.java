import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] trees = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            trees[i] = Integer.parseInt(st.nextToken());
        }

        long left = 0, right = Arrays.stream(trees).max().getAsInt();

        while (left <= right) {
            long mid = left + (right - left) / 2;
            long wooddeuk = 0;
            for (int i = 0; i < n; i++) {
                if (trees[i] >= mid) {
                    wooddeuk += (trees[i] - mid);
                }
            }
            if (wooddeuk >= m) {
                left = mid + 1;
            }else {
                right = mid - 1;
            }

        }

        System.out.println(right);
    }
}