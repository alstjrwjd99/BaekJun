def solution(N, road, K):
    answer = 0
    INF = float('inf')
    dist = [[INF] * N for _ in range (N)]
    for r in road:
        dist[r[0]-1][r[1]-1] = min(r[2],dist[r[0]-1][r[1]-1])
        dist[r[1]-1][r[0]-1] = min(r[2],dist[r[1]-1][r[0]-1])
    
    for k in range (N):
        for i in range (N):
            for j in range (N):
                dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])
    
    for i in range (1,N):
        if dist[0][i] <= K:
            answer +=1 
    return answer+1