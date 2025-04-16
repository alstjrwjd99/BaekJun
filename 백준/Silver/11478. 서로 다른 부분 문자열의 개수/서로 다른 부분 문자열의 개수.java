import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String totalString = br.readLine();
        HashSet<String> made = new HashSet<>();

        for (int len = 0; len <= totalString.length(); len++) {
            for (int i = 0; i < totalString.length() - len; i++) {
                String sb = totalString.substring(i, i + len + 1) ;
                made.add(sb);
            }
        }

        System.out.println(made.size());
    }

}