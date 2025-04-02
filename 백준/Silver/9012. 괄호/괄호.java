import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            String input = br.readLine();
            if (isVPS(input)){
                System.out.println("YES");
            }else {
                System.out.println("NO");
            }
        }
    }
    static boolean isVPS(String input) {
        ArrayDeque<Character> stack = new ArrayDeque<Character>();
        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);
            if (c == '(') {
                stack.add(c);
            }else if (!stack.isEmpty() && c == ')') {
                stack.poll();
            }else {
                return false;
            }
        }
        if (stack.isEmpty()) {
            return true;
        }
        return false;
    }
}
