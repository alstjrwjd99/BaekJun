from sys import stdin
from collections import deque

input = stdin.readline

R, C = map(int, input().split())
graph = []

pos_j = []  # 지훈 위치
pos_f = []  # 불 위치
for i in range(R):
    tmp = list(input())
    for j in range(C):
        if tmp[j] == "J":
            pos_j.append((i, j))
        elif tmp[j] == "F":
            pos_f.append((i, j))
    graph.append(tmp)


q = deque()
q.append((pos_j[0][0], pos_j[0][1], "J"))  # 지훈이가 먼저 이동
graph[pos_j[0][0]][pos_j[0][1]] = 0

if len(pos_f) != 0:
    for (r, c) in pos_f:
        q.append((r, c, "F"))
        graph[r][c] = "#"


def bfs():
    dx = [-1, 1, 0, 0]  # 상하좌우
    dy = [0, 0, -1, 1]
    while q:
        x, y, case = q.popleft()
        if case == "J" and (x == 0 or y == 0 or x == R - 1 or y == C - 1):  # 탈출가능
            if graph[x][y] == "#":
                continue
            return graph[x][y] + 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if graph[nx][ny] != "#" and case == "F":
                    graph[nx][ny] = "#"
                    q.append((nx, ny, "F"))
                elif graph[nx][ny] == "." and case == "J" and graph[x][y] != "#":
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny, "J"))
    return "IMPOSSIBLE"


print(bfs())