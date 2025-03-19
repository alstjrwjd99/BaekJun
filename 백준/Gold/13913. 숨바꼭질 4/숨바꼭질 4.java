import java.util.*;
import java.io.*;

public class Main {
    static int[] parent = new int[100001]; // 경로를 저장할 배열

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken()); // 수빈이 위치
        int k = Integer.parseInt(st.nextToken()); // 동생 위치

        boolean[] visited = new boolean[100001];
        visited[n] = true;
        Arrays.fill(parent, -1);  // 초기값 설정

        ArrayDeque<Subin> queue = new ArrayDeque<>();
        queue.add(new Subin(n, 0));

        while (!queue.isEmpty()) {
            Subin sub = queue.poll();

            if (sub.place == k) {
                System.out.println(sub.time);
                printPath(n, k); // 경로 출력
                break;
            }

            // 이동 조건 (범위를 벗어나지 않도록 검사)
            if (sub.place + 1 <= 100000 && !visited[sub.place + 1]) {
                queue.add(new Subin(sub.place + 1, sub.time + 1));
                visited[sub.place + 1] = true;
                parent[sub.place + 1] = sub.place; // 경로 기록
            }

            if (sub.place - 1 >= 0 && !visited[sub.place - 1]) {
                queue.add(new Subin(sub.place - 1, sub.time + 1));
                visited[sub.place - 1] = true;
                parent[sub.place - 1] = sub.place; // 경로 기록
            }

            if (sub.place * 2 <= 100000 && !visited[sub.place * 2]) {
                queue.add(new Subin(sub.place * 2, sub.time + 1));
                visited[sub.place * 2] = true;
                parent[sub.place * 2] = sub.place; // 경로 기록
            }
        }
    }

    // 경로 역추적 메서드
    static void printPath(int start, int end) {
        ArrayList<Integer> path = new ArrayList<>();
        int current = end;

        while (current != start) {
            path.add(current);
            current = parent[current];
        }
        path.add(start);

        Collections.reverse(path); // 경로 순서 정렬
        for (int p : path) {
            System.out.print(p + " ");
        }
    }
}

class Subin {
    int place;
    int time;

    public Subin(int place, int time) {
        this.place = place;
        this.time = time;
    }
}