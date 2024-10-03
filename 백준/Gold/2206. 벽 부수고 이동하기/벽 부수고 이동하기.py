import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
maps = [
    list(map(int, input().strip()))
    for _ in range(N)
]

dxs, dys = (-1, 0, 1, 0), (0, -1, 0, 1)

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

visited = set([(0, 0, False)])  # 방문 상태는 (x, y, 벽을 부순 상태)로 관리
queue = deque([(0, 0, False, 1)])  # (x, y, 벽을 부순 상태, 이동 횟수)

find = -1
while queue:
    x, y, is_broken, move_cnt = queue.popleft()
    
    if (x, y) == (N-1, M-1):
        find = move_cnt
        break

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        
        if in_range(nx, ny):
            if not is_broken and (nx, ny, False) not in visited:
                if maps[nx][ny] == 0:  # 길일 때
                    queue.append((nx, ny, False, move_cnt + 1))
                    visited.add((nx, ny, False))
                elif maps[nx][ny] == 1:  # 벽일 때
                    queue.append((nx, ny, True, move_cnt + 1))
                    visited.add((nx, ny, True))
            elif is_broken and (nx, ny, True) not in visited:
                if maps[nx][ny] == 0:  # 길일 때만 이동 가능
                    queue.append((nx, ny, True, move_cnt + 1))
                    visited.add((nx, ny, True))

print(find)