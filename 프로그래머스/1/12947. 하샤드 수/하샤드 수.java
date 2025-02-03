import java.util.*;

class Solution {
    public boolean solution(int x) {
        int hashad = sum(convertToArray(x)); // 숫자를 배열로 변환 후 sum 계산
        return x % hashad == 0;  // Harshad 수 판별
    }

    private int sum(int[] list) {
        int total = 0;
        for (int num : list) {
            total += num;
        }
        return total;
    }

    private int[] convertToArray(int x) {
        String numStr = Integer.toString(x);
        int[] digits = new int[numStr.length()];
        for (int i = 0; i < numStr.length(); i++) {
            digits[i] = numStr.charAt(i) - '0'; // 문자 → 숫자 변환
        }
        return digits;
    }
}