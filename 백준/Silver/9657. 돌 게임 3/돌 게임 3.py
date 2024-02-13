n = int(input())
win = ['SK','CY']

if n>4:
  dp = [0] * (n+1)
else :
  dp = [0] * (6)
dp[1] = 0
dp[2] = 1
dp[3] = 0
dp[4] = 0
for i in range (5, n+1):
  if (dp[i-1] or dp[i-3]  or dp[i-4]) == 1 :
    dp[i] = 0
  else:
    dp[i] = 1
print(win[dp[n]])