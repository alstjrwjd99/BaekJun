import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        long x = Long.parseLong(st.nextToken());
        long y = Long.parseLong(st.nextToken());

        int base = (int)(y * 100 / x);
        if (base >= 99) {
            System.out.println(-1);
            return;
        }

        long left = 1;
        long right = 1_000_000_000;
        long answer = -1;

        while (left <= right) {
            long mid = (left + right) / 2;
            long nx = x + mid;
            long ny = y + mid;
            int rate = (int)(ny * 100 / nx);

            if (rate > base) {
                answer = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        System.out.println(answer);
    }
}