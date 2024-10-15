def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                # 삼각형의 첫 번째 열은 바로 위의 값만 더할 수 있음
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i])-1:
                # 삼각형의 마지막 열은 바로 위 왼쪽의 값만 더할 수 있음
                triangle[i][j] += triangle[i-1][j-1]
            else:
                # 그 외의 경우, 위 왼쪽과 위 오른쪽 중 큰 값을 더함
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    
    return max(triangle[-1])