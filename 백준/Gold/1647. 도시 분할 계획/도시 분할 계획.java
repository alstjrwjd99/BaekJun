import java.io.*;
import java.util.*;

class Main {

    static int[] parent;

    static class House {
        int my;
        int neighbour;
        int price;
        House(int my, int neighbour, int price) {
            this.my = my;
            this.neighbour = neighbour;
            this.price = price;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken()); 
        int m = Integer.parseInt(st.nextToken()); 

        parent = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            parent[i] = i;
        }

        List<House> houses = new ArrayList<>();

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            houses.add(new House(a, b, c));
        }

        houses.sort(Comparator.comparingInt(o -> o.price));

        int answer = 0;
        int maxEdge = 0;

        for (House h : houses) {
            if (find(h.my) != find(h.neighbour)) {
                union(h.my, h.neighbour);
                answer += h.price;
                maxEdge = Math.max(maxEdge, h.price);
            }
        }

        System.out.println(answer - maxEdge);
    }

    static int find(int x){
        if (parent[x] != x){
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    static void union(int a, int b){
        int rootA = find(a);
        int rootB = find(b);
        if (rootA < rootB) parent[rootB] = rootA;
        else parent[rootA] = rootB;
    }
}