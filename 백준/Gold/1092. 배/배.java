import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        Integer[] crane = new Integer[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            crane[i] = Integer.parseInt(st.nextToken());
        }

        int m = Integer.parseInt(br.readLine());
        List<Integer> boxes = new ArrayList<>();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            boxes.add(Integer.parseInt(st.nextToken()));
        }

        Arrays.sort(crane, Collections.reverseOrder());
        boxes.sort(Collections.reverseOrder());

        if (boxes.get(0) > crane[0]) {
            System.out.println(-1);
            return;
        }

        int time = 0;
        while (!boxes.isEmpty()) {
            int idx = 0;
            for (int i = 0; i < n; ) {
                if (idx == boxes.size()) break;
                if (crane[i] >= boxes.get(idx)) {
                    boxes.remove(idx);
                    i++;
                } else {
                    idx++;
                }
            }
            time++;
        }

        System.out.println(time);
    }
}