def solution(beginning, target):
    n, m = len(beginning), len(beginning[0])
    answer = float('inf')

    # 특정 열의 반전 상태를 탐색
    for col_mask in range(1 << m):  # 2^m 개의 열 반전 조합
        flipped = [[beginning[i][j] for j in range(m)] for i in range(n)]

        # 열 반전 적용
        for j in range(m):
            if col_mask & (1 << j):  # j번째 열 반전
                for i in range(n):
                    flipped[i][j] ^= 1

        # 각 행의 반전 여부 결정
        row_mask = 0
        for i in range(n):
            if flipped[i] != target[i]:  # 현재 행이 타겟과 다르면 반전 필요
                row_mask |= (1 << i)

        # 반전된 결과 확인
        valid = True
        for i in range(n):
            for j in range(m):
                if (row_mask & (1 << i)) > 0:  # i번째 행 반전
                    flipped[i][j] ^= 1
                if flipped[i][j] != target[i][j]:  # 타겟과 불일치
                    valid = False
                    break
            if not valid:
                break

        # 유효한 경우 최소 반전 횟수 갱신
        if valid:
            flips = bin(col_mask).count('1') + bin(row_mask).count('1')  # 반전 횟수 계산
            answer = min(answer, flips)

    return -1 if answer == float('inf') else answer