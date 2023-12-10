n = int(input())

def dyPro(n):
  if n <= 3 :
    return n
  dp = [0] * (n+2)
  dp[1] = 1
  dp[2] = 2
  dp[3] = 3 

  for i in range (4,n+1):
    dp[i] = dp[i-3] + i //2 + 1
  return dp[n]

for _ in range (n):
  m = int(input())
  print(dyPro(m))