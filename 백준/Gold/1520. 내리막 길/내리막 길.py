'''
이미 방문 했던 루트가 있을 경우 -> 또 탐색할 필요는 없음
dfs -> 방문한 노드가 있으면 그자리에서 answer + 1, 종료
'''
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

dxs, dys = (-1, 1, 0, 0), (0, 0, 1, -1)

# 메모이제이션을 위한 dp 배열, -1로 초기화하여 아직 방문하지 않은 것을 표시
dp = [[-1] * M for _ in range(N)]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

def dfs(x, y):
    # 도착점에 도달한 경우
    if (x, y) == (N - 1, M - 1):
        return 1
    
    # 이미 계산된 경로가 있는 경우
    if dp[x][y] != -1:
        return dp[x][y]
    
    # 경로의 수 초기화
    dp[x][y] = 0
    
    # 현재 위치에서 이동할 수 있는 다음 위치 탐색
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and maps[nx][ny] < maps[x][y]:
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]

# 시작점에서 dfs 탐색 시작
answer = dfs(0, 0)
print(answer)