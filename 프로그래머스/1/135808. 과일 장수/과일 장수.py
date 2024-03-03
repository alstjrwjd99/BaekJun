def solution(k, m, score):
    answer = 0
    score.sort()
    while len(score) >= m:
        for i in range (m):
            apple = score.pop()
            if i == m-1:
                less = apple
        answer += less * m
    return answer