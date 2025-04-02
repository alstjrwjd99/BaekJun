/*
* 문제 해결 방안
* 1. 쌍 구하기 함수 getCombinations() ( for문 2개도 써도 무방 )
* 2. 두개 단어 입력 받아 숌스러운 단어인지 판별 함수 isShoum(word1, word2)
* */

import java.io.*;
import java.util.*;

public class Main {
    static List<String> words = new ArrayList<>();
    static int answer = 0;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            words.add(br.readLine());
        }

        getCombinations(new ArrayList<>(), 0);
        System.out.println(answer);
    }

    static void getCombinations(List<String> made, int idx) {
        if (made.size() == 2) {
            if (isShoum(made.get(0), made.get(1))) {
                answer++;
            }
            return;
        }

        for (int i = idx; i < words.size(); i++) {
            made.add(words.get(i));
            getCombinations(made, i + 1);
            made.remove(made.size() - 1);
        }
    }

    static boolean isShoum(String word1, String word2) {
        int len = word1.length();
        Map<Character, Character> map = new HashMap<>();
        Map<Character, Character> reverseMap = new HashMap<>();

        for (int i = 0; i < len; i++) {
            char c1 = word1.charAt(i);
            char c2 = word2.charAt(i);

            if (map.containsKey(c1)) {
                if (map.get(c1) != c2) {
                    return false;
                }
            } else {
                map.put(c1, c2);
            }

            if (reverseMap.containsKey(c2)) {
                if (reverseMap.get(c2) != c1) {
                    return false;
                }
            } else {
                reverseMap.put(c2, c1);
            }
        }

        return true;
    }
}