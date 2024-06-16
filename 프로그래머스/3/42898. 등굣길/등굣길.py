def solution(M, N, puddles):
    roads = [[0 for _ in range(M+1)] for _ in range(N+1)]   #dp

    for puddle in puddles:
        roads[puddle[1]][puddle[0]] = -1           #puddle 위치 표시

    for i in range(1,N+1):
        for j in range(1,M+1):
            if i==1 and j==1:                 
                roads[1][1] = 1                    #시작 = 1
            elif roads[i][j] == -1:                 # puddle일경우 0으로 바꾸기
                roads[i][j] = 0
            else:                                  #dp 더하기
                roads[i][j] = roads[i-1][j]+roads[i][j-1]
    return roads[N][M] % 1000000007