class Solution {
    public int solution(int slice, int n) {
        int answer = 0;
        int i = 0;
        while (slice * i < n){
            answer ++;
            i ++;
        }
        return answer;
    }
}