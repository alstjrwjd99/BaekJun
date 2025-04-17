import java.io.*;
import java.util.*;

public class Main {
    static int maxLen = 0;
    static int idx1 = -1, idx2 = -1;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        String[] words = new String[N];
        for (int i = 0; i < N; i++) {
            words[i] = br.readLine();
        }

        HashMap<String, Object> root = new HashMap<>();
        root.put("children", new HashMap<String, Object>());

        for (int i = 0; i < N; i++) {
            insert(root, words, i);
        }

        System.out.println(words[idx1]);
        System.out.println(words[idx2]);
    }

    static void insert(HashMap<String, Object> root, String[] words, int index) {
        HashMap<String, Object> node = root;
        int depth = 0;

        for (char ch : words[index].toCharArray()) {
            depth++;
            HashMap<String, Object> children = (HashMap<String, Object>) node.get("children");

            if (!children.containsKey(String.valueOf(ch))) {
                HashMap<String, Object> newNode = new HashMap<>();
                newNode.put("children", new HashMap<String, Object>());
                newNode.put("firstIndex", index);
                children.put(String.valueOf(ch), newNode);
            } else {
                HashMap<String, Object> nextNode = (HashMap<String, Object>) children.get(String.valueOf(ch));
                int firstIdx = (int) nextNode.get("firstIndex");

                if (firstIdx != index) {
                    update(firstIdx, index, depth);
                }
            }

            node = (HashMap<String, Object>) children.get(String.valueOf(ch));
        }

        node.put("*", null);
    }

    static void update(int a, int b, int len) {
        if (len > maxLen ||
                (len == maxLen && a < idx1) ||
                (len == maxLen && a == idx1 && b < idx2)) {
            maxLen = len;
            idx1 = a;
            idx2 = b;
        }
    }
}