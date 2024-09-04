import sys
input = sys.stdin.readline

n = int(input())

def solution(n):
    if n < 3:
        return 1
    
    answer, start, end, current_sum  = 1, 1, 1, 1

    while start <= (n // 2 + 1):
        if current_sum == n:
            answer += 1
            current_sum -= start
            start += 1
        elif current_sum < n:
            end += 1
            current_sum += end
        else:
            current_sum -= start
            start += 1
    return answer

print(solution(n))