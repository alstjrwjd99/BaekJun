import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

class Pair {
    int first;
    int second;

    Pair(int first, int second) {
        this.first = first;
        this.second = second;
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        ArrayDeque<Pair> dq = new ArrayDeque<>();
        StringBuilder sb = new StringBuilder();

        // 덱에 Pair 저장
        for (int i = 0; i < N; i++) {
            Pair p = new Pair(Integer.parseInt(st.nextToken()), i + 1);
            dq.add(p);
        }

        // 첫 번째 풍선 처리
        Pair pair = dq.removeFirst();
        sb.append(pair.second).append(' ');

        // 반복문으로 풍선 터뜨리기 로직 수행
        while (!dq.isEmpty()) {
            int move = pair.first;

            // 양수일 경우 (오른쪽 이동)
            if (move > 0) {
                for (int j = 0; j < move - 1; j++) {
                    dq.addLast(dq.removeFirst());
                }
            }
            // 음수일 경우 (왼쪽 이동)
            else {
                for (int j = 0; j < Math.abs(move); j++) {
                    dq.addFirst(dq.removeLast());
                }
            }

            // 풍선 제거 및 결과 추가
            pair = dq.removeFirst();
            sb.append(pair.second).append(' ');
        }

        System.out.println(sb.toString().trim()); // 공백 제거 후 출력
    }
}