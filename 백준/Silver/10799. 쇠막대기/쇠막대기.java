import java.io.*;
import java.util.*;

public class Main {
    static int answer = 0;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        ArrayDeque<String> stack = new ArrayDeque<>();
        String s = br.readLine();
        for(int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if(c == '(') {
                stack.push(s);
            }else{
                stack.pop();
                if (s.charAt(i-1) == '(') {
                    answer += stack.size();
                }else{
                    answer += 1;
                }
            }
        }
        System.out.println(answer);

    }

}