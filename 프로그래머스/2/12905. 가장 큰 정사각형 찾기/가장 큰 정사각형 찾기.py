def solution(board):
    answer = 0    
    col = len(board)
    row = len(board[0])
    dp = [[0] * row for _ in range (col)]
    
    for i in range (col):
        for j in range (row):
            if board[i][j] == 1:
                dp[i][j] += 1
                if i<1 or j<1 :
                    continue
                dp[i][j] = min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j]) + 1
    for a in dp:
        # print(a)
        answer = max(answer,max(a))
    return answer**2