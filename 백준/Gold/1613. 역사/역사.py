import sys
input = sys.stdin.readline

n, k = map(int, input().split())
accident = [
    tuple(map(int, input().split())) 
    for _ in range(k)
]

q = int(input())
question = [
    tuple(map(int, input().split())) 
    for _ in range(q)
]

INF = float('inf')
dist = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dist[i][i] = 0

for a, b in accident:
    dist[a][b] = 1

# 플로이드 워셜 알고리즘
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

for u, v in question:
    if dist[u][v] != INF:
        print(-1)
    elif dist[v][u] != INF:
        print(1)
    else:
        print(0)