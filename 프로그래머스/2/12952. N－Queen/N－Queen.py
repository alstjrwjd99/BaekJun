def solution(n):
    global answer
    answer = 0
    
    # 열과 대각선 사용 여부를 체크하는 배열
    is_queen_col = [False] * n
    is_queen_up_down_diag = [False] * (2 * n - 1)
    is_queen_down_up_diag = [False] * (2 * n - 1)
    
    def dfs(row):
        global answer
        if row == n:
            answer += 1
            return
        
        for column in range(n):
            if not is_queen_col[column] and not is_queen_up_down_diag[row + column] and not is_queen_down_up_diag[row - column + n - 1]:
                is_queen_col[column] = is_queen_up_down_diag[row + column] = is_queen_down_up_diag[row - column + n - 1] = True
                dfs(row + 1)
                is_queen_col[column] = is_queen_up_down_diag[row + column] = is_queen_down_up_diag[row - column + n - 1] = False

    dfs(0)
    return answer