N = int(input())
work = []

for i in range (N):
  work.append(list(map(int, input().split())))
dp = [0] * (N+1)

for i in range(N):
  for j in range(i+work[i][0],N+1):
    if dp[j] < dp[i] + work[i][1]:
      dp[j] = dp[i] + work[i][1]

print(dp[-1])