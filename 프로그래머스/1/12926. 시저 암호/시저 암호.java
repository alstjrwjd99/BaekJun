class Solution {
    public String solution(String s, int n) {
        StringBuilder sb = new StringBuilder();
        char[] list = s.toCharArray();
        for(char ch:list){
            if (ch == ' '){
                sb.append(' ');
                continue;
            }
            int chr = (int) ch;
            int changed = chr + n;
            if (chr >=65 && chr <= 90){
                if (changed > 90){
                    changed -= 26;
                }
            }else if (chr >=97 && chr <= 122) {
                if (changed > 122){
                    changed -= 26;
                }
            }
            sb.append((char) changed);
        }
        return sb.toString();
    }
}