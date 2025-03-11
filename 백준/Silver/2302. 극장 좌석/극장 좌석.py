import sys
input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())

before = 0
answer = 1

dp = [0] * (n + 2)
dp[1] = 1
if n >= 2:
    dp[2] = 2
for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

for _ in range(m):
    vip = int(input().strip())
    count = vip - before - 1
    if count > 0:
        answer *= dp[count]
    before = vip

count = n - before
if count > 0:
    answer *= dp[count]

print(answer)