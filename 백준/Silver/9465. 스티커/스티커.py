T = int(input())

def sticky(sticker, dp):
  dp[0][0] = sticker[0][0]
  dp[1][0] = sticker[1][0]
  if n == 1:
    return max(dp[0][0], dp[1][0])

  dp[0][1] = sticker[0][1] + sticker[1][0]
  dp[1][1] = sticker[1][1] + sticker[0][0]
  if n == 2:
    return max(dp[0][1], dp[1][1])
  
  for i in range (2,n):
    dp[0][i] = max(dp[1][i-2], dp[1][i-1]) + sticker[0][i]
    dp[1][i] = max(dp[0][i-2], dp[0][i-1]) + sticker[1][i]

  return max(dp[0][-1], dp[1][-1])

for _ in range(T):
    n = int(input())
    dp = [[0] * n for _ in range (2)]
    sticker = [list(map(int, input().split())) for _ in range(2)]
    print(sticky(sticker,dp))
