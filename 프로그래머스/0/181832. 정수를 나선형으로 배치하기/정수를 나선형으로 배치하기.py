def solution(n):
    answer = [[0] * n for _ in range (n)]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    global num,x,y
    x,y,num = 0,0,1
    def round(n):
        global num,x,y
        for i in range (4):
            for _ in range (n-1):
                answer[x][y] = num
                x += dx[i]
                y += dy[i]
                num += 1
        x += 1
        y += 1

    for i in range (n//2):
        round(n-i*2)
    if n % 2 == 1:
        answer[(n//2)][(n//2)] = n*n

    return answer
