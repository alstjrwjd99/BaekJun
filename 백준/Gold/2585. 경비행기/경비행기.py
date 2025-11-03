import sys
import math
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

start = (0, 0)
goal = (10000, 10000)

def require_oil(x1, y1, x2, y2):
    dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return math.ceil(dist / 10)

def bfs(points, start, goal, tank, k):
    nodes = [start] + points + [goal]
    n = len(nodes)
    graph = [[] for _ in range(n)]

    for i in range(n):
        x1, y1 = nodes[i]
        for j in range(i + 1, n):
            x2, y2 = nodes[j]
            if require_oil(x1, y1, x2, y2) <= tank:
                graph[i].append(j)
                graph[j].append(i)

    dist = [-1] * n
    queue = deque([0])
    dist[0] = 0

    while queue:
        cur = queue.popleft()
        if cur == n - 1:
            break
        for nxt in graph[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                queue.append(nxt)

    if dist[n - 1] == -1:
        return False

    return dist[n - 1] - 1 <= k

left, right = 0, 10**11
answer = -1

while left <= right:
    mid = (left + right) // 2
    if bfs(points, start, goal, mid, k):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)