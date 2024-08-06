def solution(n):
    global answer
    answer = 0
    
    # 열과 대각선 사용 여부를 체크하는 배열
    col = [False] * n
    diag1 = [False] * (2 * n - 1)
    diag2 = [False] * (2 * n - 1)
    
    def dfs(row):
        global answer
        if row == n:
            answer += 1
            return
        
        for c in range(n):
            if not col[c] and not diag1[row + c] and not diag2[row - c + n - 1]:
                col[c] = diag1[row + c] = diag2[row - c + n - 1] = True
                dfs(row + 1)
                col[c] = diag1[row + c] = diag2[row - c + n - 1] = False

    dfs(0)
    return answer

n = int(input())
print(solution(n))