from collections import deque
import sys
input = sys.stdin.readline

dx = [1,2,2,1,-1,-2,-2,-1]
dy = [-2,-1,1,2,-2,-1,1,2]

def bfs(i,j):
    q = deque([(i,j,0)])
    visited.add((i,j))
    while q :
        x,y,z = q.popleft()
        z += 1 
        for i in range (8):
            nx = x + dx[i]
            ny = y + dy[i]   
   
            if 0<= nx < I and 0<= ny < I and (nx,ny) not in visited:
                if (nx,ny) == (px,py):
                    print(z)
                    return
                q.append((nx,ny,z))
                visited.add((nx,ny))

T = int(input())
for _ in range (T):
    I = int(input())
    cx,cy = map(int,input().split())
    px,py = map(int,input().split())
    if (cx,cy) == (px,py):
        print(0)
        continue
    visited = set()
    bfs(cx,cy)

    