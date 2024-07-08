from collections import deque

def solution(maps):
    answer = 0
    for i in range (len(maps)):
        for j in range (len(maps[0])):
            if maps[i][j] == 'S':
                start = (i,j,0)
            if maps[i][j] == 'L':
                lever = (i,j,0)
            
    dxs,dys = [0,0,1,-1],[1,-1,0,0]
    
    def in_range (x,y):
        return 0<=x<len(maps) and 0<=y<len(maps[0])
    
    def bfs1(e,start):
        queue = deque([start])
        visited = set()
        visited.add((start[0],start[1]))
        while queue:
            x,y,cnt = queue.popleft()
            for dx,dy in zip(dxs,dys):
                nx = x+dx
                ny = y+dy
                if in_range(nx,ny) and (nx,ny) not in visited:
                    if maps[nx][ny] == 'O' or maps[nx][ny] == 'E':
                        queue.append((nx,ny,cnt+1))  
                        visited.add((nx,ny))
                    elif maps[nx][ny] == e:
                        return cnt + 1
        return -1
    
    def bfs2(e,start):
        queue = deque([start])
        visited = set()
        visited.add((start[0],start[1]))
        while queue:
            x,y,cnt = queue.popleft()
            for dx,dy in zip(dxs,dys):
                nx = x+dx
                ny = y+dy
                if in_range(nx,ny) and (nx,ny) not in visited:
                    if maps[nx][ny] == 'O' or maps[nx][ny] == 'S':
                        queue.append((nx,ny,cnt+1))  
                        visited.add((nx,ny))
                    elif maps[nx][ny] == e:
                        return cnt + 1
        return -1
    
    gotolever = bfs1('L',start)
    if gotolever == -1: return -1
    else : answer += gotolever
    
    gotoexit = bfs2('E',lever)
    if gotoexit == -1 : return -1
    else : answer += gotoexit
    
    return answer