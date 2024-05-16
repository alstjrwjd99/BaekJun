'''
bfs 미로찾기
'''
from collections import deque
T = 10

def bfs():
    ans = 0
    queue = deque([(1,1)])
    visited = set()
    visited.add((1,1))
    while queue:
        x,y = queue.popleft()
        if maze[x][y] == 3:
            ans = 1
            break
        for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            nx, ny = x + dx , y +dy
            if 0<=nx<15 and 0<=ny<15 and (nx,ny) not in visited and (maze[nx][ny] == 0 or maze[nx][ny] == 3) :
                queue.append((nx,ny))
                visited.add((nx,ny))
    return ans
 
for test_case in range (1, T+1):
    tc = int(input())
    maze = [
        list(map(int,input().rstrip()))    
        for _ in range (16)
    ]

    print(f"#{test_case} {bfs()}")