from collections import deque

def solution(board):
    answer = 0
    n = len(board)
    m = len(board[0])
    
    s_x, s_y = -1, -1
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                s_x, s_y = i, j 
            elif board[i][j] == 'G':
                end = (i, j)
                
    def in_range(x, y):
        return 0 <= x < n and 0 <= y < m
    
    queue = deque([(s_x, s_y, 0)])
    visited = set([(s_x, s_y)])
    
    while queue:
        x, y, cnt = queue.popleft()
        for dx, dy in zip((-1, 0, 1, 0), (0, 1, 0, -1)):
            nx, ny = x + dx, y + dy
            while in_range(nx, ny) and board[nx][ny] != 'D':
                nx += dx
                ny += dy
            nx -= dx
            ny -= dy
            if (nx, ny) == end:
                return cnt + 1
            if (nx, ny) not in visited:
                queue.append((nx, ny, cnt + 1))
                visited.add((nx, ny))
    
    return -1