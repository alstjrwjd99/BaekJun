function solution(n) {
    let answer = 0;
    let left = 1, right = 1, total = 1;

    while (left <= n / 2) {
        if (total < n) {
            right++;
            total += right;
        } else if (total > n) {
            total -= left;
            left++;
        } else {
            answer++;
            total -= left;
            left++;
        }
    }

    return answer + 1;
}