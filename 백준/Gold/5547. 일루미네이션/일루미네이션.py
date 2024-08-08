import sys
from collections import deque
input = sys.stdin.readline

w, h = map(int, input().split())
graph = [[0] * (w + 2)]
for _ in range(h):
    graph.append([0] + list(map(int, input().split())) + [0])
graph.append([0] * (w + 2))

dy = [0, 1, 1, 0, -1, -1]
dx = [[1, 0, -1, -1, -1, 0], [1, 1, 0, -1, 0, 1]]

def in_range(x, y):
    return 0 <= x < h + 2 and 0 <= y < w + 2

def bfs(y, x):
    queue = deque([(y, x)])
    visited = [[False for _ in range(w + 2)] for _ in range(h + 2)]
    visited[y][x] = True
    cnt = 0
    while queue:
        y, x = queue.popleft()
        for i in range(6):
            ny,nx = y + dy[i], x + dx[y % 2][i]
            if in_range(ny, nx):
                if graph[ny][nx] == 0 and not visited[ny][nx]:
                    queue.append((ny, nx))
                    visited[ny][nx] = True
                elif graph[ny][nx] == 1:
                    cnt += 1
    return cnt

print(bfs(0, 0))