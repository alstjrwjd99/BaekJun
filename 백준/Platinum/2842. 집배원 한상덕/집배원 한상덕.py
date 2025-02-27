import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
town = [input().strip() for _ in range(n)]
fatigue = [list(map(int, input().split())) for _ in range(n)]

dxs = [-1, 1, 0, 0, -1, -1, 1, 1]
dys = [0, 0, -1, 1, -1, 1, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def get_fat_values():
    vals = set()
    for i in range(n):
        for j in range(n):
            vals.add(fatigue[i][j])
    return sorted(vals)

fat_values = get_fat_values()

def get_post_office():
    for i in range(n):
        for j in range(n):
            if town[i][j] == 'P':
                return i, j
    return None

p_x, p_y = get_post_office()

def count_houses():
    cnt = 0
    for i in range(n):
        for j in range(n):
            if town[i][j] == 'K':
                cnt += 1
    return cnt

total_K = count_houses()

def bfs(start_x, start_y, low, high):
    if not (low <= fatigue[start_x][start_y] <= high):
        return False

    visited = [[False] * n for _ in range(n)]
    q = deque()
    q.append((start_x, start_y))
    visited[start_x][start_y] = True
    count = 0

    while q:
        x, y = q.popleft()
        if town[x][y] == 'K':
            count += 1
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[nx][ny]:
                if low <= fatigue[nx][ny] <= high:
                    visited[nx][ny] = True
                    q.append((nx, ny))
    return count == total_K

# 후보 구간 [L, L+D] 중에서 시작점 'P'의 피로도가 포함되고 BFS로 모든 'K'를 방문할 수 있는 구간이 있는지 확인
def canReach(D):
    for L in fat_values:
        R = L + D
        if not (L <= fatigue[p_x][p_y] <= R):
            continue
        if bfs(p_x, p_y, L, R):
            return True
    return False

low_D = 0
high_D = fat_values[-1] - fat_values[0]  
result = high_D

while low_D <= high_D:
    mid = (low_D + high_D) // 2
    if canReach(mid):
        result = mid
        high_D = mid - 1
    else:
        low_D = mid + 1

print(result)