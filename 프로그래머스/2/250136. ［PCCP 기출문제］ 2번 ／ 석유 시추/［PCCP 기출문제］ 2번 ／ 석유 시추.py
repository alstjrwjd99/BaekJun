from collections import deque

def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])
    dxs = [-1,1,0,0]
    dys = [0,0,1,-1]
    result = [0 for i in range(m+1)]
    visited = [[0 for i in range(m)] for j in range(n)]

    def in_range (x,y):
        return 0<=x<n and 0<=y<m
    
    def bfs(i,j):
        visited[i][j] = 1
        queue = deque([(i,j)]) 
        min_y, max_y =j, j
        count = 0
        while queue:
            x,y = queue.popleft()
            
            min_y = min(min_y, y)
            max_y = max(max_y, y)
            count += 1
            for dx,dy in zip(dxs, dys):
                nx , ny =  x + dx , y + dy
                if in_range(nx,ny) and land[nx][ny] == 1 and visited[nx][ny] == 0:
                    queue.append((nx,ny))
                    visited[nx][ny] = 1
        for i in range(min_y, max_y+1):
            result[i] += count
            
        return visited
            
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and land[i][j] == 1:
                bfs(i,j)
    answer = max(result)
    return answer