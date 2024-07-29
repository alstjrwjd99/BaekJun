from collections import deque

def solution(q1, q2):
    answer = -1

    ql = [deque(q1), deque(q2)]
    sl = [sum(q1), sum(q2)]
    
    # 홀수인 경우
    if sum(sl) % 2 != 0:
        return -1
    
    count = 0
    # l = 2 * sum([ len(v) for v in ql ])
    l = 2 * sum(map(len,ql))
    while count < l:
        if sl[0] == sl[1]:
            answer = count
            break

        idx = 1 if sl[0] < sl[1] else 0

        c = ql[idx].popleft()
        ql[1-idx].append(c)

        sl[idx] -= c
        sl[1-idx] += c
        count += 1
    
    return answer