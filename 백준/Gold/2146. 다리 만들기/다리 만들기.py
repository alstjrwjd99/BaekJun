import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
maps = [ list(map(int,input().split())) for _ in range (n)] 
dxs, dys = [0,1,0,-1],[1,0,-1,0]
islands = []

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def bfs(i,j):
    queue = deque([(i,j)])
    visited = set([(i,j)])
    while queue:
        x,y = queue.popleft()
        for dx,dy in zip(dxs, dys):
            nx ,ny = x + dx , y + dy
            if in_range(nx,ny) and (nx,ny) not in visited and maps[nx][ny] == 1:
                visited.add((nx,ny))
                queue.append((nx,ny))
    
    islands.append(visited)

for i in range (n):
    for j in range (n):
        if maps[i][j] == 0 : continue
        another_island = False
        for island in islands:
            if (i,j) in island :
              another_island = True  
        if not another_island:
            bfs(i,j)
            


def find_island(my_island):
    queue = deque()
    visited = set()
    for i,j in my_island:
        visited.add((i,j))
        for dx,dy in zip(dxs, dys):
            nx ,ny = i + dx , j + dy
            if in_range(nx,ny) and (nx,ny) and maps[nx][ny] == 0:
                queue.append((nx,ny,1))
                visited.add((nx,ny))
    
    while queue:
        x,y,cnt = queue.popleft()
        for dx,dy in zip(dxs, dys):
            nx ,ny = x + dx , y + dy
            if in_range(nx,ny) and (nx,ny) not in visited :
                if maps[nx][ny] == 0:
                    visited.add((nx,ny))
                    queue.append((nx,ny,cnt + 1))
                elif maps[nx][ny] == 1:
                    return(cnt)

answer = float('inf')          
for my_island in islands:
    answer = min(answer, find_island(my_island))

print(answer)