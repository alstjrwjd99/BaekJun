def solution(matrix_sizes):
    n = len(matrix_sizes)
    dp = [[0] * n for _ in range(n)] 

    dimensions = [matrix_sizes[0][0]] + [matrix[1] for matrix in matrix_sizes]

    for length in range(2, n + 1): 
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + dimensions[i] * dimensions[k + 1] * dimensions[j + 1]
                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n - 1]