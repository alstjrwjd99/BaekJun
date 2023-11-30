N = int(input())

for _ in range (N):
  k = int(input())
  n = int(input())
  dp = [[i+1 for i in range (n+1)] for j in range(k+1)]
  for floor in range (1,k+1):
    for ho in range (1,n+1):
      dp[floor][ho] = dp[floor-1][ho] + dp[floor][ho-1]
  print(dp[k][n-1])