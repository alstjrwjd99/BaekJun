import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();

        String[] splitted = s.split("-");

        int answer = 0;

        for (int i = 0; i < splitted.length; i++) {
            String[] addParts = splitted[i].split("\\+");
            int sum = 0;
            for (String numStr : addParts) {
                sum += Integer.parseInt(numStr);
            }

            if (i == 0) {
                answer += sum;
            } else {
                answer -= sum;
            }
        }

        System.out.println(answer);
    }
}