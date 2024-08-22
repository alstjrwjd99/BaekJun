from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    grid = [[0] * 101 for _ in range (101)]
    
    for x1,y1,x2,y2 in rectangle :
        x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2
        for i in range (x1,x2+1):
            for j in range (y1,y2+1):
                grid[i][j] = 1

    for x1,y1,x2,y2 in rectangle :
        x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2
        for i in range (x1+1,x2):
            for j in range (y1+1,y2):
                grid[i][j] = 0

    queue = deque([(characterX * 2,characterY * 2,0)])
    visited = set([(characterX * 2,characterY * 2)])
    dxs, dys = (-1,1,0,0) , (0,0,1,-1)
    
    def in_range (x,y):
        return 0<=x<101 and 0<=y<101
    
    while queue :
        x,y ,cnt= queue.popleft()
        for dx,dy in zip ( dxs, dys):
            nx,ny = x + dx , y + dy
            if in_range (nx,ny) and (nx,ny) not in visited and grid[nx][ny] == 1:
                queue.append((nx,ny,cnt+1))
                visited.add((nx,ny))
                
                if (nx,ny) == (itemX * 2,itemY * 2):
                    answer = cnt // 2 + 1
                    break
    
    return answer