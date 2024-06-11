def solution(prices):
    answer = [i for i in range (len(prices)-1,-1,-1)]
    stack = []
    for i in range (len(prices)):
        while stack and prices[i] < stack[-1][0]:
            top,idx = stack.pop()
            answer[idx] = i - idx
        stack.append((prices[i],i))
    return answer