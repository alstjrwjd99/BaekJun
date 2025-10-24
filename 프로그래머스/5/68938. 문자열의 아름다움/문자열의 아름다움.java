import java.util.*;

class Solution {
    static class Node {
        long samePoint = 0; // 추가해야 하는 누적 포인트
        long difPoint = 0;  // 추가해야 하는 누적 포인트
        long sameCnt = 0;
        long difCnt = 0;
        int ed = 0;
    }

    public long solution(String s) {
        long answer = 0;
        char prevChar = s.charAt(0);
        boolean[] isFirst = new boolean[26];
        long[] nuHap = new long[300001]; // 1~i까지 누적 합
        Map<Integer, Map<Integer, Integer>> sMap = new HashMap<>(); // alpha : [길이 : 개수]
        Node[] nodeInfo = new Node[26];
        for (int i = 0; i < 26; i++) nodeInfo[i] = new Node();

        int conCnt = 1; // 연속으로 몇 개 나왔는지

        for (int i = 1; i < s.length(); i++) {
            nuHap[i] = nuHap[i - 1] + i;
            int prevAlpha = prevChar - 'a';
            int prevI = i - 1;

            if (s.charAt(i) == prevChar) { // 이전 문자와 현재 문자가 같다면
                conCnt += 1;
            } else { // 다르다면 갱신
                if (!isFirst[prevAlpha]) { // 처음이라면
                    isFirst[prevAlpha] = true;
                    nodeInfo[prevAlpha].difPoint = nuHap[prevI] - nuHap[conCnt - 1];
                    nodeInfo[prevAlpha].sameCnt = conCnt;
                    nodeInfo[prevAlpha].difCnt = prevI - conCnt + 1;
                    nodeInfo[prevAlpha].ed = prevI;

                    sMap.putIfAbsent(prevAlpha, new HashMap<>());
                    sMap.get(prevAlpha).put(conCnt, sMap.get(prevAlpha).getOrDefault(conCnt, 0) + 1);
                } else {
                    int eed = nodeInfo[prevAlpha].ed;
                    // 다른 알파벳 포인트 갱신
                    nodeInfo[prevAlpha].difPoint += (prevI - eed) * nodeInfo[prevAlpha].difCnt
                            + (nuHap[prevI - eed - 1] - nuHap[conCnt - 1]);
                    // 같은 알파벳 포인트 갱신
                    nodeInfo[prevAlpha].samePoint += (prevI - eed) * nodeInfo[prevAlpha].sameCnt;

                    sMap.putIfAbsent(prevAlpha, new HashMap<>());
                    sMap.get(prevAlpha).put(conCnt, sMap.get(prevAlpha).getOrDefault(conCnt, 0) + 1);

                    nodeInfo[prevAlpha].sameCnt += conCnt;
                    nodeInfo[prevAlpha].difCnt = prevI + 1 - nodeInfo[prevAlpha].sameCnt;
                    nodeInfo[prevAlpha].ed = prevI;
                }
                prevChar = s.charAt(i);
                conCnt = 1;
            }

            int nowAlpha = s.charAt(i) - 'a';
            long ccct = 0;

            int eed = nodeInfo[nowAlpha].ed;

            if (!isFirst[nowAlpha]) { // 방문 전
                ccct = nuHap[i] - nuHap[conCnt - 1];
            } else {
                ccct += nodeInfo[nowAlpha].difPoint + (i - eed) * nodeInfo[nowAlpha].difCnt;
                ccct += nuHap[i - eed - 1] - nuHap[conCnt - 1];
            }

            if (sMap.containsKey(nowAlpha)) {
                for (Map.Entry<Integer, Integer> entry : sMap.get(nowAlpha).entrySet()) {
                    int len = entry.getKey();
                    int cnt = entry.getValue();
                    if (conCnt < len) {
                        ccct += (nuHap[(i - conCnt) - (eed - len + 1)] - nuHap[i - (eed + 1)]) * cnt;
                    }
                    ccct += (long) (i - (eed + 1)) * cnt * Math.min(conCnt, len);
                }
            }

            ccct += nodeInfo[nowAlpha].samePoint;
            answer += ccct;
        }

        return answer;
    }
}