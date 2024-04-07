from collections import deque
import sys
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(i,j,color):
    q = deque([(i,j)])
    visited.add((i,j))
    while q :
        x,y = q.popleft()
        for i in range (4):
            nx = x + dx[i]
            ny = y + dy[i]       
            if 0<= nx < n and 0<= ny < n and graph[nx][ny] == color and (nx,ny) not in visited:
                q.append((nx,ny))
                visited.add((nx,ny))

n = int(input())

graph = []

for _ in range (n):
    graph.append(list(input()))

visited = set()
answer = 0
for i in range (n):
    for j in range (n):
        if (i,j) not in visited:
            bfs(i,j,graph[i][j])
            answer += 1
print(answer)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'
visited.clear()
answer = 0
for i in range (n):
    for j in range (n):
        if (i,j) not in visited:
            bfs(i,j,graph[i][j])
            answer += 1
print(answer)
