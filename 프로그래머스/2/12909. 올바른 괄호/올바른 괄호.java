import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        Deque<Character> stack = new ArrayDeque<>();

        for(char bracket : s.toCharArray()){
            if (bracket == '('){
                stack.push(bracket);
            }else {
                if (!stack.isEmpty()){
                    stack.pop();
                }else {
                    return false;
                }
            }
        }
        if (!stack.isEmpty()){
            return false;
        }
        return answer;
    }

}