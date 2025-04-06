import java.io.*;
import java.util.*;

public class Main {
    private static int answer;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);

        int x = Integer.parseInt(br.readLine());

        int s = 0, e = n - 1;

        while (s < e){
            int sum = arr[s] + arr[e];
            if (sum > x){
                e --;
            }
            else if (sum < x){
                s ++;
            }
            else{
                answer ++;
                s++;
            }
        }
        System.out.println(answer);
    }
}