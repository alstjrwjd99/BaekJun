import java.io.*;
import java.util.*;

public class Main {
    static Map<String, String> parent;
    static Map<String, Integer> size;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testCase = Integer.parseInt(br.readLine());

        for (int t = 0; t < testCase; t++) {
            int f = Integer.parseInt(br.readLine());
            parent = new HashMap<>();
            size = new HashMap<>();

            for (int i = 0; i < f; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                String a = st.nextToken();
                String b = st.nextToken();

                union(a, b);
                System.out.println(size.get(find(a))); 
            }
        }
    }

    static String find(String x) {
        if (!parent.containsKey(x)) {
            parent.put(x, x);
            size.put(x, 1);
        }

        if (!x.equals(parent.get(x))) {
            parent.put(x, find(parent.get(x)));
        }

        return parent.get(x);
    }

    static void union(String a, String b) {
        String pa = find(a);
        String pb = find(b);

        if (!pa.equals(pb)) {
            parent.put(pb, pa);
            size.put(pa, size.get(pa) + size.get(pb));
        }
    }
}