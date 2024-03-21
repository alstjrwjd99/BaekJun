def solution(n):
    answer = 1
    for i in range (1,n//2+1):
        tmp = 0
        while True:
            tmp += i
            i += 1
            if tmp == n:
                answer += 1
            if tmp > n:
                break
    return answer