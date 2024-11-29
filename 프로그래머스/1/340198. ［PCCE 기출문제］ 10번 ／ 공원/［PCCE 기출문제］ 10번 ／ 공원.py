def solution(mats, park):
    mats.sort(reverse=True)
    rows, cols = len(park), len(park[0])
    dp = [[0] * cols for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            if park[i][j] == '-1':
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    for mat in mats:
        for i in range(rows):
            for j in range(cols):
                if dp[i][j] >= mat:  # 해당 크기의 정사각형 발견
                    return mat
    return -1