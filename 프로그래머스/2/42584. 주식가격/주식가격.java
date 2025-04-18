/*
1. 스택에 맨위보다 높은 주식 (가격, 인덱스) 담기
2. 맨위보다 낮은 가격을 만날 때는 while 문을 쓰면서 pop하고 answer 갱신
*/
import java.util.*;

import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        Deque<Stock> stack = new ArrayDeque<>();

        for (int i = 0; i < prices.length; i++) {
            while (!stack.isEmpty() && prices[i] < stack.peek().price) {
                Stock top = stack.pop();
                answer[top.idx] = i - top.idx;
            }
            stack.push(new Stock(prices[i], i));
        }

        while (!stack.isEmpty()) {
            Stock top = stack.pop();
            answer[top.idx] = prices.length - top.idx - 1;
        }

        return answer;
    }

    class Stock {
        int price;
        int idx;
        Stock(int price, int idx) {
            this.price = price;
            this.idx = idx;
        }
    }
}