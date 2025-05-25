import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int[] share = new int[n];
        for (int i = 0; i < n; i++) {
            share[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(share);

        long left = 1;
        long right = share[n - 1] - share[0];
        long answer = 0;

        while (left <= right) {
            long mid = (left + right) / 2;

            int cnt = 1;
            int last = share[0];

            for (int i = 1; i < n; i++) {
                if (share[i] - last >= mid) {
                    cnt++;
                    last = share[i];
                }
            }

            if (cnt >= c) {
                answer = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        System.out.println(answer);
    }
}