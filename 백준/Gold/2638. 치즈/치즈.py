import sys
input = sys.stdin.readline

n, m = map(int, input().split())
paper = [list(map(int,input().split())) for _ in range (n)]
visited = [[False] * m for _ in range (n)]

from collections import deque

def in_range(x,y):
    return 0 <= x < n and 0 <= y < m
    
def bfs(i,j):
    queue = deque([(i,j)])
    touched = set()
    deleted = []
    while queue:
        x,y = queue.popleft()
        
        for dx, dy in zip((-1,0,1,0),(0,1,0,-1)):
            nx = x + dx
            ny = y + dy
            if in_range(nx,ny) and not visited[nx][ny]:
                if paper[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                else :
                    if (nx,ny) in touched :
                        deleted.append((nx,ny))
                    else :
                        touched.add((nx,ny))
    for i,j in deleted:
        paper[i][j] = 0
    
answer = 0
flag = True
while flag:
    bfs(0,0)
    visited = [[False] * m for _ in range (n)]
    answer += 1
    
    flag = False
    for i in range (n):
        for j in range (m):
            if paper[i][j] == 1 :
                flag = True
                break

print(answer)