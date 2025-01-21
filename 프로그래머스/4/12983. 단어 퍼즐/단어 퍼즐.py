def solution(strs, t):
    dp = [float('inf')] * (len(t) + 1) 
    dp[0] = 0 
    max_len = 5  
    
    for i in range(1, len(t) + 1):
        for j in range(1, max_len + 1):
            if i - j >= 0 and t[i-j:i] in strs:
                dp[i] = min(dp[i], dp[i-j] + 1)
    
    return dp[len(t)] if dp[len(t)] != float('inf') else -1