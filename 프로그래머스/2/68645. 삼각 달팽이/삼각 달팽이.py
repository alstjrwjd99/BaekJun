def solution(n):
    ret = []
    answer = [[0]* i for i in range (1,n+1)]
    snail = 1
    x,y=0,0
    dx = (1,0,-1)
    dy = (0,1,-1)
    i=0
    while snail != n*(n+1)/2+1:
        answer[x][y] = snail
        nx,ny = x+dx[i%3], y+dy[i%3]
        if nx >= n:
            i+=1
            nx,ny = x+dx[i%3], y+dy[i%3]
        elif ny>=len(answer[nx]):
            i+=1
            nx,ny = x+dx[i%3], y+dy[i%3]
        elif answer[nx][ny] != 0:
            i+=1
            nx,ny = x+dx[i%3], y+dy[i%3]
        snail += 1
        x,y=nx,ny
    
    for a in answer:
        for j in (a):
            ret.append(j)
    return ret
