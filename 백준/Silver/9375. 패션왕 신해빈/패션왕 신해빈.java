import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testCase = Integer.parseInt(br.readLine());

        for (int t = 0; t < testCase; t++) {
            HashMap<String, ArrayList<String>> map = new HashMap<>();
            int n = Integer.parseInt(br.readLine());

            for (int i = 0; i < n; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                String cloth = st.nextToken();
                String kind = st.nextToken();

                map.putIfAbsent(kind, new ArrayList<>());
                map.get(kind).add(cloth);
            }

            int answer = 1;
            for (Map.Entry<String, ArrayList<String>> entry : map.entrySet()) {
                answer *= (entry.getValue().size() + 1);
            }

            System.out.println(answer - 1);
        }
    }
}