/*
* 자식 -> 부모 탐색
* dp[i] : i번째에 최소 얼리어답터의 수
*
* 부모가 얼리 -> 자식은 얼리어도 되고 아니어도됨
* 부모가 얼리아님 -> 자식들 중 하나는 무조건 얼리
* */

import java.io.*;
import java.util.*;

public class Main {
    static HashMap<Integer, List<Integer>> map = new HashMap<>();
    static int N;
    static int[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        dp = new int[N + 1][2];
        for (int[] row : dp) Arrays.fill(row, -1);

        for (int i = 0; i < N - 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            map.putIfAbsent(u, new ArrayList<>());
            map.putIfAbsent(v, new ArrayList<>());
            map.get(u).add(v);
            map.get(v).add(u);
        }

        int answer = Math.min(dfs(1, -1, false), dfs(1, -1, true));
        System.out.println(answer);

    }

    static int dfs(int node, int parent, boolean isEarly) {
        int state = isEarly ? 1 : 0;
        if (dp[node][state] != -1) return dp[node][state];

        int res = isEarly ? 1 : 0;

        for (int next : map.getOrDefault(node, new ArrayList<>())) {
            if (next == parent) continue;

            if (isEarly) {
                res += Math.min(dfs(next, node, true), dfs(next, node, false));
            } else {
                res += dfs(next, node, true);
            }
        }

        return dp[node][state] = res;
    }
}