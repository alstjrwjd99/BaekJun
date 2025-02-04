class Solution {
    public int solution(long n) {
        String three = Long.toString(n, 3);
        String reversed = new StringBuilder(three).reverse().toString();
        return Integer.parseInt(reversed, 3);
    }
}