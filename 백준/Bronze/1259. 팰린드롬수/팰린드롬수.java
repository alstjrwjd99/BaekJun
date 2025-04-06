import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            String word = br.readLine();
            if (word.equals("0")) {
                break;
            }

            String reversed = new StringBuilder(word).reverse().toString();
            if (word.equals(reversed)) {
                System.out.println("yes");
            } else {
                System.out.println("no");
            }
        }
    }
}