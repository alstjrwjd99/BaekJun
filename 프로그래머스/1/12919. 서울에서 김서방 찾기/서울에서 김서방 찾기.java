class Solution {
    public String solution(String[] seoul) {
        int index = -1;

        // 배열에서 "Kim"의 위치 찾기
        for (int i = 0; i < seoul.length; i++) {
            if (seoul[i].equals("Kim")) {
                index = i;
                break;
            }
        }

        // 문자열 포맷팅하여 반환
        return "김서방은 " + index + "에 있다";
    }
}