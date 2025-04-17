import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int stage = 1;

        while (true) {
            int answer = 0;
            int n = Integer.parseInt(br.readLine());
            if(n == 0){
                break;
            }

            String[] names = new String[n];
            HashMap<String, String> map = new HashMap<>();
            HashSet<String> visited = new HashSet<>();

            for (int i = 0; i < n; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                String from = st.nextToken();
                String to = st.nextToken();
                map.put(from, to);
                names[i] = from;
            }

            for (int i = 0; i < n; i++) {
                String start = names[i];
                if (!visited.contains(start)) {
                    visited.add(start);
                    String next = map.get(start);
                    while (!next.equals(start)) {
                        visited.add(next);
                        next = map.get(next);
                    }
                    answer++;
                }
            }
            System.out.println(stage + " " + answer);
            stage++;
        }
    }
}