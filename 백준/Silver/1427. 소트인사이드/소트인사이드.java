/*
* 문제 해결 방안
* 문자열을 입력받아 정렬
* */

import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] arr = br.readLine().toCharArray();
        Arrays.sort(arr);
        String result = new StringBuilder(new String(arr)).reverse().toString();

        System.out.println(result);
    }
}