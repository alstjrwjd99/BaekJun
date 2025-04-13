import java.io.*;
import java.util.*;

public class Main {
    static ArrayDeque<Integer> queue = new ArrayDeque<Integer>();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String cmd = st.nextToken();
            if (cmd.equals("push")) {
                push(Integer.parseInt(st.nextToken()));
            } else if (cmd.equals("pop")) {
                pop();
            } else if (cmd.equals("size")) {
                size();
            } else if (cmd.equals("empty")) {
                empty();
            } else if (cmd.equals("front")) {
                front();
            }else if (cmd.equals("back")) {
                back();
            }
        }

    }

    static void push(int val){
        queue.add(val);
    }

    static void pop(){
        if(queue.isEmpty()){
            System.out.println(-1);
        }else{
            System.out.println(queue.pop());
        }
    }

    static void size(){
        System.out.println(queue.size());
    }

    static void empty(){
        if (queue.isEmpty()){
            System.out.println(1);
        }else {
            System.out.println(0);
        }
    }

    static void front(){
        if (queue.isEmpty()){
            System.out.println(-1);
        }else {
            System.out.println(queue.getFirst());
        }
    }

    static void back(){
        if (queue.isEmpty()){
            System.out.println(-1);
        }else {
            System.out.println(queue.getLast());
        }
    }
}