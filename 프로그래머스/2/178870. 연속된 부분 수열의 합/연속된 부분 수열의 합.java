class Solution {
    public int[] solution(int[] sequence, int k) {
        int n = sequence.length;
        int[] prefix = sequence.clone();
        for (int i = 1; i < n; i++) {
            prefix[i] += prefix[i - 1];
        }

        int left = 0, right = 0;
        int[] answer = {0, n};

        while (right < n) {
            int sum = prefix[right] - (left > 0 ? prefix[left - 1] : 0);

            if (sum == k) {
                if (answer[1] - answer[0] > right - left) {
                    answer[0] = left;
                    answer[1] = right;
                }
                left++;
            } else if (sum > k) {
                left++;
            } else {
                right++;
            }

            if (left > right) right = left;
        }

        return answer;
    }
}