'''
2중 for문 돌면서 해당하는 조건 영역 더하기
'''
T = int(input())
                
for test_case in range(1, T+1):
    N = int(input())
    answer = 0
    grid = [
        list(input())
        for _ in range (N)
    ]
    for i in range (N):
        if i <= N//2:
            start = N//2 - i
            end = N//2 + i    
        else :
            start = i - N//2
            end = N - i + N//2 -1

        answer += (sum(map(int,grid[i][start:end+1])))
    
    print(f'#{test_case} {answer}')
