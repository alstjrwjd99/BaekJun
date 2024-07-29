from collections import deque

def solution(q1, q2):
    answer = -1
    
    q1 = deque(q1)
    q2 = deque(q2)
    s1 = sum(q1)
    s2 = sum(q2)

    count = 0
    l = 2 * sum([len(q1), len(q2)])
    while count < l:
        if s1 < s2:
            c2 = q2.popleft()
            q1.append(c2)

            s2 -= c2
            s1 += c2
        elif s1 > s2:
            c1 = q1.popleft()
            q2.append(c1)

            s1 -= c1
            s2 += c1
        else:
            answer = count
            break
        count += 1
    
    return answer