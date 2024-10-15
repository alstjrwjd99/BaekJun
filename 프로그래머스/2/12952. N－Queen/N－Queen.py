def solution(n):
    answer = 0

    # 각 열, 대각선을 방문했는지 기록하는 배열
    col = [False] * n
    up_diag = [False] * (2 * n - 1)  # 오른쪽 위에서 왼쪽 아래로 가는 대각선
    down_diag = [False] * (2 * n - 1)  # 왼쪽 위에서 오른쪽 아래로 가는 대각선

    def n_queen(row):
        nonlocal answer
        if row == n:
            answer += 1
            return

        # 열을 하나씩 확인하며 퀸을 놓을 수 있는지 확인
        for j in range(n):
            if not col[j] and not up_diag[row + j] and not down_diag[row - j + (n - 1)]:
                # 퀸을 놓을 수 있으면 마크
                col[j] = True
                up_diag[row + j] = True
                down_diag[row - j + (n - 1)] = True

                # 다음 행으로 이동
                n_queen(row + 1)

                # 백트래킹: 다시 퀸을 놓지 않은 상태로 되돌리기
                col[j] = False
                up_diag[row + j] = False
                down_diag[row - j + (n - 1)] = False

    # 첫 번째 행부터 시작
    n_queen(0)

    return answer