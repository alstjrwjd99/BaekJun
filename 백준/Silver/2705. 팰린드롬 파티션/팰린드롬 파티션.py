import sys
input = sys.stdin.readline

T = int(input())

dp = [0] * 1001
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 2

for i in range (4, 1001):
    side = 0
    while side * 2 <= i:
        dp[i] += dp[side]
        side += 1
for _ in range (T):
    n = int(input())
    print(dp[n])