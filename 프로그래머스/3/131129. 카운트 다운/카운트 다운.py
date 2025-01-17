def solution(target):
    dp = [[float('inf'), 0] for _ in range(target + 1)]
    dp[0] = [0, 0]  
    scores = set()
    
    for i in range(1, 21):
        scores.add(i)      
        scores.add(i * 2)  
        scores.add(i * 3)  
    scores.add(50)         
    scores = sorted(scores)

    for i in range(1, target + 1):
        for score in scores:
            if i < score:
                break
            if dp[i][0] > dp[i - score][0] + 1:
                dp[i][0] = dp[i - score][0] + 1
                dp[i][1] = dp[i - score][1] + (1 if score <= 20 or score == 50 else 0)
            # 싱글/불의 개수가 더 많으면 갱신
            elif dp[i][0] == dp[i - score][0] + 1:
                dp[i][1] = max(dp[i][1], dp[i - score][1] + (1 if score <= 20 or score == 50 else 0))

    return dp[target]