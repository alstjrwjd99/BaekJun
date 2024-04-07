import sys
input = sys.stdin.readline
N = int(input())
schedule = []
for _ in range (N):
    schedule.append(list(map(int,input().split())))
dp = [0] * (N+1)
for i in range (N):
    for j in range (i + schedule[i][0],N+1):
        dp[j] = max(dp[i] + schedule[i][1],dp[j])
print(dp[-1])