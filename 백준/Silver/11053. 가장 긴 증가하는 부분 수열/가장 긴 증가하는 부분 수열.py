A = int(input())
numlist = list(map(int,input().split()))
dp = [1]*A
for i in range (A):
  for j in range (i):
    if numlist[i] > numlist[j]:
      dp[i] = max(dp[i],dp[j]+1)
print(max(dp))