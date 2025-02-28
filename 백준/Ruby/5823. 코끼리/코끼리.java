import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static long L;
    // 각 코끼리의 현재 위치를 저장 (인덱스: 코끼리 번호)
    static int[] pos;
    // TreeMap: key=위치, value=해당 위치에 있는 코끼리 수
    static TreeMap<Integer, Integer> posMap;
    // 현재 서로 다른 인접 위치들 사이에서, gap > L 인 경우의 개수
    static long gapCount = 0;
    
    public static void main(String[] args) throws Exception {
        // 빠른 입출력을 위해 BufferedReader, PrintWriter 사용
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        N = Integer.parseInt(st.nextToken());
        L = Long.parseLong(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        
        pos = new int[N];
        posMap = new TreeMap<>();
        // 초기 위치 입력 (이미 정렬되어 있음)
        for (int i = 0; i < N; i++) {
            pos[i] = Integer.parseInt(br.readLine().trim());
            posMap.put(pos[i], posMap.getOrDefault(pos[i], 0) + 1);
        }
        // 초기 gapCount 계산: TreeMap의 distinct 키들에 대해, 인접 두 키의 차이가 L보다 크면 gap++
        Integer prev = null;
        for (Integer key : posMap.keySet()) {
            if (prev != null) {
                if ((long)key - prev > L) {
                    gapCount++;
                }
            }
            prev = key;
        }
        
        // 각 update마다 필요한 카메라 수 = gapCount + 1
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int idx = Integer.parseInt(st.nextToken());
            int newPos = Integer.parseInt(st.nextToken());
            update(idx, newPos);
            pw.println(gapCount + 1);
        }
        pw.flush();
        pw.close();
    }
    
    // update(i, newPos): 코끼리 i의 위치를 newPos로 옮기고, gapCount를 갱신
    static void update(int i, int newPos) {
        int oldPos = pos[i];
        // 만약 변화가 없다면 바로 리턴
        if (oldPos == newPos) return;
        
        // 1. oldPos 제거 처리
        int freqOld = posMap.get(oldPos);
        if (freqOld == 1) {
            // oldPos가 TreeMap에서 완전히 제거되는 경우
            Integer pred = posMap.lowerKey(oldPos);
            Integer succ = posMap.higherKey(oldPos);
            // 기존 oldPos와 pred 사이의 gap 제거
            if (pred != null) {
                if ((long)oldPos - pred > L) {
                    gapCount--;
                }
            }
            // 기존 oldPos와 succ 사이의 gap 제거
            if (succ != null) {
                if ((long)succ - oldPos > L) {
                    gapCount--;
                }
            }
            // 새롭게 pred와 succ 사이의 gap가 생길 수 있음
            if (pred != null && succ != null) {
                if ((long)succ - pred > L) {
                    gapCount++;
                }
            }
            posMap.remove(oldPos);
        } else {
            // oldPos에 여러 코끼리가 있었다면 단순히 빈도 감소 (gap 변화 없음)
            posMap.put(oldPos, freqOld - 1);
        }
        
        // 2. newPos 추가 처리
        if (posMap.containsKey(newPos)) {
            // 이미 newPos에 코끼리가 있다면 빈도만 증가
            posMap.put(newPos, posMap.get(newPos) + 1);
        } else {
            // newPos가 새로 추가되는 경우, 주변 키를 찾아 gap 갱신
            Integer pred = posMap.lowerKey(newPos);
            Integer succ = posMap.higherKey(newPos);
            // pred와 newPos 사이의 gap 새로 형성
            if (pred != null) {
                if ((long)newPos - pred > L) {
                    gapCount++;
                }
            }
            // newPos와 succ 사이의 gap 새로 형성
            if (succ != null) {
                if ((long)succ - newPos > L) {
                    gapCount++;
                }
            }
            // 만약 pred와 succ 모두 존재한다면, 원래 pred와 succ 사이의 gap는 제거됨
            if (pred != null && succ != null) {
                if ((long)succ - pred > L) {
                    gapCount--;
                }
            }
            posMap.put(newPos, 1);
        }
        // 3. 코끼리 i의 위치 업데이트
        pos[i] = newPos;
    }
}