def solution(rows, columns, queries):
    answer = []
    # 초기 행렬을 생성합니다.
    matrix = [[i + j * columns for i in range(1, columns + 1)] for j in range(rows)]

    # 각 쿼리 처리
    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1  # 인덱스 조정 (0 기반 인덱스)
        temp = matrix[x1][y1]  # 회전할 값 임시 저장
        min_value = temp
        
        # 왼쪽 열 아래로 이동
        for i in range(x1, x2):
            matrix[i][y1] = matrix[i + 1][y1]
            min_value = min(min_value, matrix[i][y1])
        
        # 아래 행 오른쪽으로 이동
        for j in range(y1, y2):
            matrix[x2][j] = matrix[x2][j + 1]
            min_value = min(min_value, matrix[x2][j])
        
        # 오른쪽 열 위로 이동
        for i in range(x2, x1, -1):
            matrix[i][y2] = matrix[i - 1][y2]
            min_value = min(min_value, matrix[i][y2])
        
        # 위쪽 행 왼쪽으로 이동
        for j in range(y2, y1, -1):
            matrix[x1][j] = matrix[x1][j - 1]
            min_value = min(min_value, matrix[x1][j])
        
        matrix[x1][y1 + 1] = temp  # 시작했던 위치에 임시 저장했던 값을 넣음
        answer.append(min_value)

    return answer