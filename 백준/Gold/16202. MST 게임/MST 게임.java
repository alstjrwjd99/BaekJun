import java.io.*;
import java.util.*;

class Main {

    static class Node {
        int myNumber;
        int neighbour;
        int price;
        Node(int myNumber, int neighbour, int price) {
            this.myNumber = myNumber;
            this.neighbour = neighbour;
            this.price = price;
        }
    }

    static class Ans{
        int answer;
        Node node;
        Ans(int answer, Node node) {
            this.answer = answer;
            this.node = node;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        List<Node> costs = new ArrayList<>();

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken()) - 1;
            int v = Integer.parseInt(st.nextToken()) - 1;

            costs.add(new Node(u,v, i + 1));
        }

        while (k-- > 0) {
            Ans ans = getMST(costs, n);
            if (ans.node == null) {
                System.out.print("0 ");
                continue;
            }
            costs.remove(ans.node);
            System.out.print(ans.answer + " ");
        }
    }

    private static Ans getMST(List<Node> costs, int n) {
        
        int[] parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;

        int answer = 0;
        int edgeCount = 0;
        Node firstUsed = null;

        for (Node node : costs) {
            int pu = find(parent, node.myNumber);
            int pv = find(parent, node.neighbour);

            if (pu != pv) {
                union(parent, pu, pv);
                answer += node.price;
                if (firstUsed == null) firstUsed = node;
                edgeCount++;
            }
            if (edgeCount == n - 1) break;
        }

        if (edgeCount != n - 1) {
            return new Ans(0, null);
        }

        return new Ans(answer, firstUsed);
    }

    private static int find(int[] parent, int x) {
        if (parent[x] != x) parent[x] = find(parent, parent[x]);
        return parent[x];
    }

    private static void union(int[] parent, int a, int b) {
        int pa = find(parent, a);
        int pb = find(parent, b);
        if (pa != pb) parent[pa] = pb;
    }
}