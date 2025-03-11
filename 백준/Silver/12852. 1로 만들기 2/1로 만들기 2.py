import sys
input = sys.stdin.readline

n = int(input().strip())

dp = [[1e9, 0] for _ in range(n + 1)]
dp[n][0] = 0
dp[n][1] = -1

for i in range(n, 0, -1):
    if i % 3 == 0 and dp[i // 3][0] > dp[i][0] + 1:
        dp[i // 3][0] = dp[i][0] + 1
        dp[i // 3][1] = i 

    if i % 2 == 0 and dp[i // 2][0] > dp[i][0] + 1:
        dp[i // 2][0] = dp[i][0] + 1
        dp[i // 2][1] = i 

    if dp[i - 1][0] > dp[i][0] + 1:
        dp[i - 1][0] = dp[i][0] + 1
        dp[i - 1][1] = i  

path = []
cur = 1
while cur != -1:
    path.append(cur)
    cur = dp[cur][1]

print(dp[1][0])
print(*reversed(path))