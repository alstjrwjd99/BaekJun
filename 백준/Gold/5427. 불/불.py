import sys
from collections import deque

# 0: 방문하지 않음 1: 상근이 방문함 2: 불이 방문함
def bfs(f_s, queue, visit): #불의 bfs인지 상근의 bfs인지 체크
    while (queue):
        x, y, time = queue.popleft()
        adjlist = [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]
        for nx, ny in adjlist:
            if nx >=0 and nx< h and ny >=0 and ny <w:
                if graph[nx][ny] == '.' or graph[nx][ny] == '@':
                    if visit[nx][ny] > time + 1:
                        visit[nx][ny] = time + 1
                        queue.append((nx, ny, visit[nx][ny]))
            elif f_s == 's':  # 상근이면 w, h를 벗어나는 순간 스탑
                print(time + 1)
                return
    if f_s == 's':
        print("IMPOSSIBLE")


tc = int(sys.stdin.readline())
for t in range(tc):
    w, h = list(map(int, sys.stdin.readline().split()))
    graph = [[0 for x in range(w)]for x in range(h)]
    visit = [[1e9 for x in range(w)]for x in range(h)]

    fqueue = deque()
    squeue = deque()
    for i in range(h):
        temp = sys.stdin.readline() # 공백이 없음
        for j in range(w):
            graph[i][j] = temp[j]
            if temp[j] == '@':
                squeue.append((i, j, 0))
            elif temp[j] == '*':
                visit[i][j] = 0
                fqueue.append((i, j, 0))
    # 불 먼저 bfs
    bfs('f', fqueue, visit)
    bfs('s', squeue, visit)
