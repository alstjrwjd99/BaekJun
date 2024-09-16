import sys
input = sys.stdin.readline

from collections import deque

T = int(input())
for test_case in range (T):
    N,M = map(int,input().split())
    q = list(map(int,input().split()))
    queue = deque()
    for i in range (N):
        queue.append((q[i],i))
    cnt,q_key = 0 , 0
    q.sort()
    max_q = q.pop()
    while queue:
        importance , idx = queue.popleft()
        if importance != max_q:
            queue.append((importance,idx))
        else :
            cnt += 1            
            if idx == M:
                print(cnt)
                break
            max_q = q.pop()