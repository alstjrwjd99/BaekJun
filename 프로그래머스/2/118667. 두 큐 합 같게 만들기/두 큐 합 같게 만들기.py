from collections import deque

def solution(queue1, queue2):
    sum1,sum2 = sum(queue1), sum(queue2)
    if (sum1 + sum2) % 2 == 1 : return -1
    
    answer = 0
    q1,q2 = deque(queue1),deque(queue2)
    while answer < 4 * (len(queue1)):
        if sum1 < sum2 : 
            bigger = q2.popleft()
            q1.append(bigger)
            sum2 -= bigger
            sum1 += bigger
        elif sum1 > sum2 : 
            bigger = q1.popleft()
            q2.append(bigger)
            sum1 -= bigger
            sum2 += bigger
        elif sum1 == sum2 :
            return answer
        answer += 1
    return -1