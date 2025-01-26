from collections import deque
import copy

def solution(maze):
    answer = 0
    q = deque()
    rvisited = [[0] * 4 for _ in range(4)]
    bvisited = [[0] * 4 for _ in range(4)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    rstart = []
    bstart = []

    n = len(maze)
    m = len(maze[0])
    
    # 빨간수레 시작위치 rstart 와 파란수레 시작위치 bstart 를 구한다
    for i in range(n):
        for j in range(m):
            cur = maze[i][j]
            if cur == 1:
                rstart = [i, j, 0]
            elif cur == 2:
                bstart = [i, j, 0]

    # bfs

    rvisited[rstart[0]][rstart[1]] = 1
    bvisited[bstart[0]][bstart[1]] = 1
    q.append([rstart, bstart,rvisited, bvisited])

    while q:
        rpos, bpos, rvi, bvi = q.popleft()
        rx, ry, rc = rpos
        bx, by, bc = bpos
        if maze[rx][ry] == 3 and maze[bx][by] == 4:
            if rc > bc :
                return rc
            else:
                return bc
        if maze[rx][ry] == 3:
            for d in range(4):
                bnx, bny = bx+dx[d], by + dy[d]
                if canGo(bnx, bny, bvi,maze, n,m):
                    if not (bnx == rx and bny == ry):
                        bvi[bnx][bny] = 1
                        q.append([[rx, ry, rc], [bnx, bny, bc+1], rvi, bvi])
        elif maze[bx][by] == 4:
            for d in range(4):
                rnx, rny = rx + dx[d], ry + dy[d]
                if canGo(rnx, rny, rvi, maze, n, m):
                    if not (rnx == bx and rny == by):
                        rvi[rnx][rny] = 1
                        q.append([[rnx, rny, rc+1], [bx, by, bc], rvi, bvi])

        else:
            for d in range(4):
                rnx, rny = rx + dx[d], ry + dy[d]
                rcvi = copy.deepcopy(rvi)
                bcvi = copy.deepcopy(bvi)
                if not (canGo(rnx, rny, rcvi, maze, n, m)):
                    continue
                for d2 in range(4):
                    bnx, bny = bx + dx[d2], by + dy[d2]
                    if canGo(bnx, bny, bcvi, maze, n, m):
                        if not (rnx == bnx and rny == bny) and not(rnx == bx and rny == by and bnx == rx and bny == ry):
                            rcvi[rnx][rny] = 1
                            bcvi[bnx][bny] = 1
                            q.append([[rnx, rny, rc+1], [bnx, bny, bc+1], rcvi, bcvi])
    return 0

def canGo(x,y,visited, maze, n, m):
    if 0 <= x < n and 0 <= y < m and maze[x][y] != 5 and visited[x][y] == 0:
        return True
    return False