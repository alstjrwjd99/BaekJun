import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = list(map(int,input().split()))
dp = [0] * (N+1)
dp[1] = arr[0]
for i in range (1,N):
  dp[i+1] = dp[i] + arr[i]
for _ in range (M):
  start, end =map(int,input().split())
  print(dp[end] - dp[start-1])