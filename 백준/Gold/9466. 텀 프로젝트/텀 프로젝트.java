import java.io.*;
import java.util.*;

public class Main {
    static int[] arr;
    static int[] visited;
    static int count;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        while (T-- > 0) {
            int n = Integer.parseInt(br.readLine());
            arr = new int[n];
            visited = new int[n];
            count = 0;

            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(st.nextToken()) - 1;
            }

            for (int i = 0; i < n; i++) {
                if (visited[i] == 0) {
                    dfs(i);
                }
            }

            System.out.println(n - count);
        }
    }

    static void dfs(int cur) {
        visited[cur] = 1;
        int next = arr[cur];

        if (visited[next] == 0) {
            dfs(next);
        } else if (visited[next] == 1) {
            count++;
            for (int i = next; i != cur; i = arr[i]) {
                count++;
            }
        }

        visited[cur] = 2;
    }
}