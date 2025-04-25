import java.util.*;

class Solution {
    public int solution(String begin, String target, String[] words) {
        if (!Arrays.asList(words).contains(target)) return 0;

        Queue<Word> queue = new ArrayDeque<>();
        Set<String> visited = new HashSet<>();

        queue.add(new Word(begin, 0));
        visited.add(begin);

        while (!queue.isEmpty()) {
            Word current = queue.poll();

            if (current.word.equals(target)) {
                return current.depth;
            }

            for (String next : words) {
                if (!visited.contains(next) && canTransform(current.word, next)) {
                    visited.add(next);
                    queue.add(new Word(next, current.depth + 1));
                }
            }
        }

        return 0;
    }

    static boolean canTransform(String a, String b) {
        int diff = 0;
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) != b.charAt(i)) diff++;
        }
        return diff == 1;
    }

    static class Word {
        String word;
        int depth;

        Word(String word, int depth) {
            this.word = word;
            this.depth = depth;
        }
    }
}