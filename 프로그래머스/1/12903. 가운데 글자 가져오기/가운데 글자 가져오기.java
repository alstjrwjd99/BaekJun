class Solution {
    public String solution(String s) {
        int len = s.length();
        if (len % 2 == 0) {
            int idx = len / 2;
            return "" + s.charAt(idx - 1) + s.charAt(idx);
        } else {
            return "" + s.charAt(len / 2);
        }
    }
}
