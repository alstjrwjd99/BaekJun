import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int[] cave1 = new int[n / 2]; 
        int[] cave2 = new int[n / 2]; 

        for (int i = 0; i < n; i++) {
            int h = Integer.parseInt(br.readLine());
            if (i % 2 == 0) {
                cave1[i / 2] = h;
            } else {
                cave2[i / 2] = h;
            }
        }

        Arrays.sort(cave1);
        Arrays.sort(cave2);

        int answer = Integer.MAX_VALUE;
        int count = 0;

        for (int i = 1; i <= c; i++) {
            int bottom = cave1.length - lowerBound(cave1, i);
            int top = cave2.length - lowerBound(cave2, c - i + 1);
            int total = bottom + top;

            if (total < answer) {
                answer = total;
                count = 1;
            } else if (total == answer) {
                count++;
            }
        }

        System.out.println(answer + " " + count);
    }

    static int lowerBound(int[] arr, int target) {
        int left = 0, right = arr.length;
        while (left < right) {
            int mid = (left + right) / 2;
            if (arr[mid] < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
}