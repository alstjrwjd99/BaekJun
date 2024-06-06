import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
vtx = [
    list(map(int,input().split()))
    for _ in range (N)
]

ans = [[0] * N for _ in range (N)]

q = deque([])

for i in range (N):
    for j in range (N):
        if vtx[i][j] == 1:
            q.append(j)
            ans[i][j] = 1
            while q:
                connect = q.popleft()
                for idx in range (N):
                    if vtx[connect][idx] == 1 and ans[i][idx] == 0:
                        q.append(idx)
                        ans[i][idx] = 1

for a in ans:
    print(*a)