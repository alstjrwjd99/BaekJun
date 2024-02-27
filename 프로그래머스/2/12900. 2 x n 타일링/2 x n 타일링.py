def solution(n):
    answer = 0
    dp = [0] * (n+2)
    dp[1] = 1
    dp[2] = 2
    for i in range (2,n+2):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    return dp[n+1]