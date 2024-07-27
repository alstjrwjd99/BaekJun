import sys
input = sys.stdin.readline

C,N = map(int,input().split())
info = [
    tuple(map(int,input().split()))
    for _ in range (N)
]

dp = [1e9] * (C+100)
dp[0] = 0
for cost,member in info:
    for money in range (member,C+100):        
        dp[money] = min(dp[money-member]+cost,dp[money]) 
            
print(min(dp[C:]))