def solution(money):
    dp = [0] * len(money)
    ddp = [0] * len(money)
    
    dp[0] = money[0]
    dp[1] = money[0]
    ddp[0] = 0
    ddp[1] = money[1]
    
    for i in range (2, len(money)):
        dp[i] = max(dp[i-1],dp[i-2] + money[i])
        ddp[i] = max(ddp[i-1],ddp[i-2] + money[i])
    return max(dp[-2],ddp[-1])