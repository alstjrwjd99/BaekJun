import java.io.*;
import java.util.*;

public class Main {
    static class ClassTime implements Comparable<ClassTime> {
        int start, end;

        public ClassTime(int start, int end) {
            this.start = start;
            this.end = end;
        }

        @Override
        public int compareTo(ClassTime o) {
            return this.start - o.start;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        ClassTime[] classes = new ClassTime[N];
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int t = Integer.parseInt(st.nextToken());
            classes[i] = new ClassTime(s, t);
        }

        Arrays.sort(classes);

        PriorityQueue<Integer> pq = new PriorityQueue<>();

        pq.offer(classes[0].end);

        for (int i = 1; i < N; i++) {
            if (pq.peek() <= classes[i].start) {
                pq.poll();
            }
            pq.offer(classes[i].end);
        }

        System.out.println(pq.size());
    }
}