def solution(sticker):
    answer = 0
    if len(sticker) == 1 : return sticker[0]
    elif len(sticker) == 2 : return max(sticker[0],sticker[1])
    dp = [0] * (len(sticker)-1)
    dp[0] = sticker[0]
    dp[1] = sticker[0]
    for i in range (2,len(sticker)-1):
        dp[i] = max(sticker[i]+dp[i-2],dp[i-1])

    dp1 = [0] * len(sticker)
    dp1[0] = 0
    dp1[1] = sticker[1]
    for i in range (2,len(sticker)):
        dp1[i] = max(sticker[i]+dp1[i-2],dp1[i-1])

    return max(dp[-1],dp1[-1])