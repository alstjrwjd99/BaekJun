from collections import deque
import sys
input = sys.stdin.readline

dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,1,-1,-1,1,-1,1]

def bfs(i,j):
    q = deque([(i,j)])
    visited.add((i,j))
    while q :
        x,y = q.popleft()
        for i in range (8):
            nx = x + dx[i]
            ny = y + dy[i]       
            if 0<= nx < h and 0<= ny < w and (nx,ny) not in visited and board[nx][ny] == 1:
                q.append((nx,ny))
                visited.add((nx,ny))
while True:
    w,h = map(int,input().split())  
    if (w,h) == (0,0):
        break
    answer = 0
    board = []
    for _ in range (h):
        board.append(list(map(int,input().split())))

    visited = set()

    for i in range (h):
        for j in range (w):
            if (i,j) not in visited and board[i][j] == 1:
                bfs(i,j)
                answer += 1
    print(answer)