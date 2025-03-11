import sys
input = sys.stdin.readline

n = int(input().strip())

class X:
    def __init__(self):
        self.value = 1e9
        self.prev = -1  # 이전 위치를 저장해 경로를 추적

dp = [X() for _ in range(n + 1)]
dp[n].value = 0  # 시작점 설정

for i in range(n, 0, -1):
    if i % 3 == 0 and dp[i // 3].value > dp[i].value + 1:
        dp[i // 3].value = dp[i].value + 1
        dp[i // 3].prev = i  # 이전 위치 기록

    if i % 2 == 0 and dp[i // 2].value > dp[i].value + 1:
        dp[i // 2].value = dp[i].value + 1
        dp[i // 2].prev = i  # 이전 위치 기록

    if dp[i - 1].value > dp[i].value + 1:
        dp[i - 1].value = dp[i].value + 1
        dp[i - 1].prev = i  # 이전 위치 기록

# 경로 복원 (Backtracking)
path = []
cur = 1
while cur != -1:
    path.append(cur)
    cur = dp[cur].prev

print(dp[1].value)
print(*reversed(path))  # 경로를 올바른 순서로 출력