from collections import deque


def solution(queue1, queue2):
    answer = 0
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    # 홀수인 경우
    if (sum1 + sum2) % 2 != 0:
        return -1
    
    while True:
        if answer == 4 * len(queue1):
            return -1
        
        if sum1 > sum2:
            value = q1.popleft()
            q2.append(value)
            sum1 -= value
            sum2 += value
        elif sum1 < sum2:
            value = q2.popleft()
            q1.append(value)
            sum1 += value
            sum2 -= value
        else:
            return answer
        answer += 1