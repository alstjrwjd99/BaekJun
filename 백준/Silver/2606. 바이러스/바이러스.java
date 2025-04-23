import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        HashMap<Integer,ArrayList<Integer>> map = new HashMap<>();
        Deque<Integer> queue = new ArrayDeque<>();
        HashSet<Integer> set = new HashSet<>();

        for(int i=0;i<m;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int computer1 = Integer.parseInt(st.nextToken());
            int computer2 = Integer.parseInt(st.nextToken());
            if (!map.containsKey(computer1)) {
                map.put(computer1, new ArrayList<>());
            }
            map.get(computer1).add(computer2);

            if (!map.containsKey(computer2)) {
                map.put(computer2, new ArrayList<>());
            }
            map.get(computer2).add(computer1);
        }


        int answer = 0;
        queue.add(1);
        set.add(1);

        while (!queue.isEmpty()){
            int virus = queue.removeFirst();
            for (int next : map.getOrDefault(virus, new ArrayList<>())) {
                if (!set.contains(next)) {
                    answer++;
                    set.add(next);
                    queue.addLast(next);
                }
            }
        }

        System.out.println(answer);
    }
}
