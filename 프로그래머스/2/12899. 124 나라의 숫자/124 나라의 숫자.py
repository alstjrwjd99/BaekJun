def solution(n):
    answer = ''
    while n:
        mod = n % 3
        if mod == 0 :
            answer = '4'+answer
            n -= 1
        else :
            answer = str(mod) + answer
        n = n // 3
    return answer