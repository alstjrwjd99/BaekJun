import java.io.*;
import java.util.*;

public class Main {
    static ArrayDeque<Integer> deque = new ArrayDeque<Integer>();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String cmd = st.nextToken();
            if (cmd.equals("push_front")) {
                push_front(Integer.parseInt(st.nextToken()));
            }else if (cmd.equals("push_back")) {
                push_back(Integer.parseInt(st.nextToken()));
            } else if (cmd.equals("pop_front")) {
                pop_front();
            } else if (cmd.equals("pop_back")) {
                pop_back();
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

    static void push_front(int val){
        deque.addFirst(val);
    }
    
    static void push_back(int val){
        deque.add(val);
    }
    static void pop_front(){
        if(deque.isEmpty()){
            System.out.println(-1);
        }else{
            System.out.println(deque.pop());
        }
    }
    static void pop_back(){
        if(deque.isEmpty()){
            System.out.println(-1);
        }else{
            System.out.println(deque.removeLast());
        }
    }

    static void size(){
        System.out.println(deque.size());
    }

    static void empty(){
        if (deque.isEmpty()){
            System.out.println(1);
        }else {
            System.out.println(0);
        }
    }

    static void front(){
        if (deque.isEmpty()){
            System.out.println(-1);
        }else {
            System.out.println(deque.getFirst());
        }
    }

    static void back(){
        if (deque.isEmpty()){
            System.out.println(-1);
        }else {
            System.out.println(deque.getLast());
        }
    }
}