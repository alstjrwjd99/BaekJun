from collections import deque
def solution(board):
    answer = 0
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    queue = deque([])
    col = len(board)
    row = len(board[0])
    dist = [[987654321 for _ in range(row)] for _ in range(col)]
    for i in range (col):
        for j in range (row):
            if board[i][j] == 'R':
                queue.append((i,j,0))
                break
    while queue:
        x,y,z = queue.popleft()
        if board[x][y] == 'G':
            return z
        for i in range (4):
            nx,ny = x,y            
            while (0 <= nx + dx[i] < col and 0 <= ny + dy[i] < row and board[ nx + dx[i] ][ny + dy[i]] != 'D'):
                nx += dx[i]
                ny += dy[i]
            if dist[nx][ny] > z+1:
                dist[nx][ny] = z+1
                queue.append((nx,ny,z+1))
    return -1