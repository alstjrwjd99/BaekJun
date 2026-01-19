import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]

dxs, dys = (0, 1, 0, -1), (1, 0, -1, 0)

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

sx = sy = -1
for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            sx, sy = i, j
            sea[i][j] = 0
            break
    if sx != -1:
        break

def find_small_fish(sx, sy, size):
    visited = [[False] * N for _ in range(N)]
    q = deque()
    q.append((sx, sy, 0))
    visited[sx][sy] = True

    fishes = []
    min_dist = None

    while q:
        x, y, dist = q.popleft()

        # 이미 먹이를 찾았고, 그보다 더 먼 레벨이면 중단
        if min_dist is not None and dist > min_dist:
            break

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if not in_range(nx, ny) or visited[nx][ny]:
                continue

            # 이동 가능 조건: 자신 크기 이하만 통과
            if sea[nx][ny] > size:
                continue

            visited[nx][ny] = True
            nd = dist + 1

            # 먹을 수 있는 물고기
            if 1 <= sea[nx][ny] < size:
                fishes.append((nd, nx, ny))
                min_dist = nd
            else:
                # 빈칸(0) 또는 같은 크기(size)는 이동만
                q.append((nx, ny, nd))

    if not fishes:
        return None
    fishes.sort()  # (거리, x, y)
    return fishes[0]  # (dist, x, y)

x, y = sx, sy
size = 2
eat_cnt = 0
answer = 0

while True:
    res = find_small_fish(x, y, size)
    if res is None:
        break

    dist, nx, ny = res
    answer += dist
    sea[nx][ny] = 0
    x, y = nx, ny

    eat_cnt += 1
    if eat_cnt == size:
        size += 1
        eat_cnt = 0

print(answer)