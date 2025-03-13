import sys
from collections import deque, defaultdict
input = sys.stdin.readline

T = int(input())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(T):
    h, w = map(int, input().split())
    building = []
    building.append(list('.' * (w+2)))
    for _ in range(h):
        line = list(input().strip())
        building.append(['.'] + line + ['.'])
    building.append(list('.' * (w+2)))
    h += 2
    w += 2

    keys_input = input().strip()
    keys = set()
    if keys_input != '0':
        keys = set(keys_input)

    ans = 0
    visited = [[False] * w for _ in range(h)]
    doors = defaultdict(list)
    dq = deque()
    dq.append((0, 0))
    visited[0][0] = True

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                cell = building[nx][ny]
                if cell == '*':
                    continue
                visited[nx][ny] = True
                if cell == '$':
                    ans += 1
                    building[nx][ny] = '.'
                if 'a' <= cell <= 'z':
                    if cell not in keys:
                        keys.add(cell)
                        while doors[cell.upper()]:
                            door_x, door_y = doors[cell.upper()].pop()
                            dq.append((door_x, door_y))
                    building[nx][ny] = '.'
                if 'A' <= cell <= 'Z':
                    if cell.lower() not in keys:
                        doors[cell].append((nx, ny))
                        continue
                    else:
                        building[nx][ny] = '.'
                dq.append((nx, ny))
    print(ans)