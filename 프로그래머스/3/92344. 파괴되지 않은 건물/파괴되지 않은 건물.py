def solution(board, skill):
    n = len(board)
    m = len(board[0])
    acc = [[0] * (m + 1) for _ in range(n + 1)]

    for type12, r1, c1, r2, c2, degree in skill:
        if type12 == 1 : degree *= -1
        acc[r1][c1] += degree
        acc[r1][c2 + 1] -= degree
        acc[r2 + 1][c1] -= degree
        acc[r2 + 1][c2 + 1] += degree

    for i in range(n):
        for j in range(m):
            if j > 0:
                acc[i][j] += acc[i][j - 1]
    for j in range(m):
        for i in range(n):
            if i > 0:
                acc[i][j] += acc[i - 1][j]

    answer = 0
    for i in range(n):
        for j in range(m):
            board[i][j] += acc[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer