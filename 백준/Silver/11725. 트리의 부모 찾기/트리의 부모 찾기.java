/**
 * https://www.acmicpc.net/problem/11725
 */

import java.io.*;
import java.util.*;

public class Main {
    static boolean[] visited;
    static int[] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        HashMap<Integer, ArrayList<Integer>> map = new HashMap<>();
        arr = new int[N + 1];
        visited = new boolean[N + 1];

        for (int i = 0; i < N-1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            map.computeIfAbsent(a, k -> new ArrayList<>()).add(b);
            map.computeIfAbsent(b, k -> new ArrayList<>()).add(a);
        }

        visited[1] = true;
        searchTree(map, 1);
        for (int i = 2; i <= N; i++) {
            System.out.println(arr[i]);
        }

    }

    static void searchTree(HashMap<Integer, ArrayList<Integer>> map, int start) {
        for (int node : map.get(start)) {
            if (!visited[node]) {
                visited[node] = true;
                arr[node] = start;
                searchTree(map, node);
            }
        }
    }
}