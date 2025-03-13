import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())
lake = [list(input().strip()) for _ in range(r)]

swans = []
water_queue = deque()
for i in range(r):
    for j in range(c):
        if lake[i][j] in ('.', 'L'):
            water_queue.append((i, j))
        if lake[i][j] == 'L':
            swans.append((i, j))

swan_start = swans[0]
swan_target = swans[1]

swan_queue = deque()
swan_queue.append(swan_start)
visited = [[False] * c for _ in range(r)]
visited[swan_start[0]][swan_start[1]] = True
swan_next = deque()

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

days = 0

def move_swan():
    while swan_queue:
        x, y = swan_queue.popleft()
        if (x, y) == swan_target:
            return True
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                visited[nx][ny] = True
                if lake[nx][ny] in ('.', 'L'):
                    swan_queue.append((nx, ny))
                elif lake[nx][ny] == 'X':
                    swan_next.append((nx, ny))
    return False

def melt_ice():
    water_next = deque()
    while water_queue:
        x, y = water_queue.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < r and 0 <= ny < c:
                if lake[nx][ny] == 'X':
                    lake[nx][ny] = '.'
                    water_next.append((nx, ny))
    return water_next

while True:
    if move_swan():
        print(days)
        break
    water_queue = melt_ice()       
    swan_queue = swan_next        
    swan_next = deque()
    days += 1