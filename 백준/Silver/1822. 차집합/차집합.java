import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());

        TreeSet<Integer> aSet = new TreeSet<>();
        HashSet<Integer> bSet = new HashSet<>();

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < A; i++) {
            Integer n = Integer.parseInt(st.nextToken());
            aSet.add(n);
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < B; i++) {
            bSet.add(Integer.parseInt(st.nextToken()));
        }

        aSet.removeAll(bSet);
        System.out.println(aSet.size());
        if(!aSet.isEmpty()){
            for (Integer n : aSet) {
                System.out.print(n+ " ");
            }
        }

    }
}