import java.io.*;
import java.util.*;

class Main {
    static class Range {
        int start, end;
        public Range(int start, int end) {
            this.start = start;
            this.end = end;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        List<Range> ranges = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            String[] input = br.readLine().split(" ");
            int a = Integer.parseInt(input[0]);
            int b = Integer.parseInt(input[1]);
            ranges.add(new Range(a, b));
        }

        ranges.sort(Comparator.comparingInt(r -> r.start));

        int answer = 0;
        int start = ranges.get(0).start;
        int end = ranges.get(0).end;

        for (int i = 1; i < ranges.size(); i++) {
            Range r = ranges.get(i);
            if (r.start <= end) {
                end = Math.max(end, r.end);
            } else {
                answer += end - start;
                start = r.start;
                end = r.end;
            }
        }
        answer += end - start;

        System.out.println(answer);
    }
}