import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        
        ArrayList<Integer> list = new ArrayList<>();
        for (int i = 1; i <= N; i++) {
            list.add(i);  // 1부터 N까지 사람을 리스트에 추가
        }
        
        StringBuilder sb = new StringBuilder();
        sb.append("<");
        
        int index = 0;  // 시작 인덱스
        while (!list.isEmpty()) {
            index = (index + K - 1) % list.size();  // 제거할 인덱스 계산
            sb.append(list.remove(index));  // 해당 인덱스의 원소 제거 및 출력
            
            if (!list.isEmpty()) {
                sb.append(", ");
            }
        }
        
        sb.append(">");
        System.out.println(sb.toString());
    }
}