from collections import deque

def solution(maps):
    queue = deque([(0,0,0)])    
    visited = set([(0,0)])
    dxs, dys = (-1,0,1,0),(0,1,0,-1)
    n = len(maps)
    m = len(maps[0])
    
    def in_range(x,y):
        return 0<=x<n and 0<=y<m and (x,y) not in visited and maps[x][y] == 1
    
    while queue:
        x,y,cnt = queue.popleft()
        for dx,dy in zip(dxs,dys):
            nx , ny = x + dx, y + dy
            if in_range(nx,ny):
                if (nx,ny) == (n-1,m-1) :
                    return cnt + 2
                queue.append((nx,ny,cnt+1))
                visited.add((nx,ny))
                
    
    return -1