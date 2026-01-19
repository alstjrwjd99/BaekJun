import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(N)]

dxs = [0, 1, 0, -1, -1, -1, 1, 1]
dys = [1, 0, -1, 0, -1, 1, -1, 1]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

dist = [[-1] * M for _ in range(N)]
q = deque()

# 모든 1을 시작점으로 큐에 넣는 멀티소스 BFS
for i in range(N):
    for j in range(M):
        if sea[i][j] == 1:
            dist[i][j] = 0
            q.append((i, j))

while q:
    x, y = q.popleft()
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))

# 0칸들의 최소거리(dist)가 계산되었으므로, 그 중 최댓값이 정답
ans = 0
for i in range(N):
    for j in range(M):
        ans = max(ans, dist[i][j])

print(ans)