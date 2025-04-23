/**
 * https://www.acmicpc.net/problem/15900
 *
 * 1. 리프 노드 갯수 구하기
 * 2. 짝수면 No 홀수면 Yes
 */

import java.io.*;
import java.util.*;

public class Main {
    static Map<Integer, ArrayList<Integer>> map = new HashMap<>();
    static boolean[] visited;
    static int answer = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        visited = new boolean[N + 1];

        for (int i = 0; i < N - 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            map.computeIfAbsent(a, k -> new ArrayList<>()).add(b);
            map.computeIfAbsent(b, k -> new ArrayList<>()).add(a);
        }

        visited[1] = true; 
        searchTree(1, 0);

        System.out.println(answer % 2 == 0 ? "No" : "Yes");
    }

    static void searchTree(int node, int depth) {
        boolean isLeaf = true;

        for (int next : map.getOrDefault(node, new ArrayList<>())) {
            if (!visited[next]) {
                isLeaf = false;
                visited[next] = true;
                searchTree(next, depth + 1);
            }
        }

        if (isLeaf) {
            answer += depth;
        }
    }
}