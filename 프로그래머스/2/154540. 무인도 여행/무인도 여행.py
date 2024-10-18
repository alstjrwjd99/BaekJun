from collections import deque

def solution(maps):
    answer = []
    
    visited = set()
    
    def in_range (x,y):
        return 0<=x<len(maps) and 0<=y<len(maps[0])
    
    def bfs(i,j):
        queue = deque([(i,j)])
        visited.add((i,j))
        eat = int(maps[i][j])
        while queue:
            x,y = queue.popleft()
            for dx,dy in zip((-1,0,1,0),(0,1,0,-1)):
                nx,ny = x + dx , y + dy
                if in_range (nx,ny) and (nx,ny) not in visited and maps[nx][ny] !='X':
                    queue.append((nx,ny))
                    visited.add((nx,ny))
                    eat += int(maps[nx][ny])
        return eat
    
    for i in range (len(maps)):
        for j in range (len(maps[0])):
            if (i,j) not in visited and maps[i][j] != 'X':
                answer.append(bfs(i,j))
                
    if not answer : return [-1]
    return sorted(answer)