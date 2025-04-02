/*
* 문제 해결 방안
* 띄어쓰기 별로 단어 뒤집기
* */

import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            String[] splitString = s.split(" ");

            for (int j = 0; j < splitString.length; j++) {
                StringBuilder word = new StringBuilder(splitString[j]);
                sb.append(word.reverse()).append(" ");
            }
            sb.append("\n");
        }

        System.out.print(sb.toString().trim());
    }
}