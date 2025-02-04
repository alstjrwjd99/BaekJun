class Solution {
    public long solution(int price, int money, int count) {
        long answer = (long) price * (count * (count + 1)) / 2 - money;
        if (answer <= 0){
            return 0;
        }
        return answer;
    }
}