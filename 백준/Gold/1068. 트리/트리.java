import java.io.*;
import java.util.*;

public class Main {

    static int answer = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] parent = new int[n];
        Node[] nodes = new Node[n];

        for (int i = 0; i < n; i++) {
            nodes[i] = new Node(i);
        }

        StringTokenizer st = new StringTokenizer(br.readLine());
        int rootIndex = -1;
        for (int i = 0; i < n; i++) {
            parent[i] = Integer.parseInt(st.nextToken());
            if (parent[i] == -1) {
                rootIndex = i;
            } else {
                nodes[parent[i]].children.add(nodes[i]);
            }
        }

        int deleteNodeNumber = Integer.parseInt(br.readLine());

        if (deleteNodeNumber == rootIndex) {
            System.out.println(0);
        } else {
            deleteNode(nodes, parent, deleteNodeNumber);
            countLeaves(nodes[rootIndex]);
            System.out.println(answer);
        }
    }

    static void deleteNode(Node[] nodes, int[] parent, int deleteIndex) {
        int parentIndex = parent[deleteIndex];
        if (parentIndex != -1) {
            nodes[parentIndex].children.removeIf(child -> child.value == deleteIndex);
        }
    }

    static void countLeaves(Node current) {
        if (current.children.isEmpty()) {
            answer++;
        } else {
            for (Node child : current.children) {
                countLeaves(child);
            }
        }
    }

    static class Node {
        int value;
        ArrayList<Node> children = new ArrayList<>();

        Node(int value) {
            this.value = value;
        }
    }
}