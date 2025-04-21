/*
슬라이딩 윈도우
1. 윈도우 크기 설정
2. 문자열 압축하는 함수 구현
*/
class Solution {
    public int solution(String s) {
        int answer = s.length();

        for (int len = 1; len <= s.length() / 2; len++) {
            answer = Math.min(answer, compressString(s, len));
        }

        return answer;
    }

    int compressString(String s, int window) {
        StringBuilder sb = new StringBuilder();
        String prev = s.substring(0, window);
        int count = 1;

        for (int i = window; i <= s.length() - window; i += window) {
            String current = s.substring(i, i + window);

            if (prev.equals(current)) {
                count++;
            } else {
                if (count > 1) {
                    sb.append(count).append(prev);
                } else {
                    sb.append(prev);
                }
                prev = current;
                count = 1;
            }
        }

        if (count > 1) {
            sb.append(count).append(prev);
        } else {
            sb.append(prev);
        }

        int remainderIndex = (s.length() / window) * window;
        if (remainderIndex < s.length()) {
            sb.append(s.substring(remainderIndex));
        }

        return sb.length();
    }
}