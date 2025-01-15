import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        
        List<Integer> list = new ArrayList<>();
        for (int i = 1; i <= N; i++) {
            list.add(i);  // 1부터 N까지 초기화
        }
        
        StringBuilder sb = new StringBuilder();
        sb.append("<");
        
        solve(list, K - 1, 0, sb);  // 재귀 호출 시작
        
        sb.append(">");
        System.out.println(sb.toString());
    }
    
    // 요세푸스 순열을 구하는 재귀 함수
    public static void solve(List<Integer> list, int k, int startIndex, StringBuilder sb) {
        if (list.isEmpty()) {
            return;  // 모든 원소가 제거되었으면 종료
        }
        
        startIndex = (startIndex + k) % list.size();  // 제거할 인덱스 계산
        sb.append(list.remove(startIndex));  // 해당 인덱스 원소 제거 및 출력
        
        if (!list.isEmpty()) {
            sb.append(", ");
        }
        
        solve(list, k, startIndex, sb);  // 재귀적으로 나머지 리스트에 대해 처리
    }
}