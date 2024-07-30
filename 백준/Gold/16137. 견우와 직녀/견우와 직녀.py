from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
INF = 1e9
answer = INF

def in_range (x,y):
    return 0<=x<n and 0<=y<n

def bfs():
    global answer
    # (x, y, 현재 시간, 오작교를 건너갔는지, 절벽 교차 여부)
    q = deque([(0, 0, 0, False, False)])
    # (x, y, 오작교를 건너갔는지) -> 최소 시간
    d = {(0, 0, False) : 0}

    while q:
        x, y, cnt, flag, cross = q.popleft() 
        # 현재 경로의 시간이 이미 최단 시간보다 크면 무시
        if cnt > answer:  
            continue
        # 목적지에 도착
        if x == n - 1 and y == n - 1:
            answer = min(answer, cnt)
            continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if in_range(nx,ny):
                if maps[nx][ny] != 0:
                    if maps[nx][ny] == 1:
                        if cnt + 1 < d.get((nx, ny, flag), INF):
                            q.append((nx, ny, cnt + 1, flag, False))
                            d[(nx, ny, flag)] = cnt + 1
                    elif not cross:  # 오작교를 아직 건너지 않았고, 해당 위치가 절벽인 경우
                        # 오작교의 주기에 맞춰 이동 시간 계산
                        if (cnt + 1) % maps[nx][ny] == 0:
                            t = cnt + 1
                        else:
                            t = cnt + (maps[nx][ny] - cnt % maps[nx][ny])
                        if t < d.get((nx, ny, flag), INF):
                            q.append((nx, ny, t, flag, True))
                            d[(nx, ny, flag)] = t
                # 현재 위치가 절벽인 경우
                else:
                    if not flag and not cross:  # 오작교를 아직 건너지 않았고, 절벽 교차도 하지 않은 경우
                        # 사각형의 네 모서리 위치를 확인하여 절벽이 교차하는지 확인
                        tmp = True
                        # (상, 우) 확인
                        if in_range(nx - 1,ny + 1):
                            if maps[nx - 1][ny] == 0 and maps[nx][ny + 1] == 0:
                                tmp = False
                        # (상, 좌) 확인
                        if in_range(nx - 1,ny - 1):
                            if maps[nx - 1][ny] == 0 and maps[nx][ny - 1] == 0:
                                tmp = False
                        # (하, 우) 확인
                        if in_range(nx + 1,ny + 1):
                            if maps[nx + 1][ny] == 0 and maps[nx][ny + 1] == 0:
                                tmp = False
                        # (하, 좌) 확인
                        if in_range(nx + 1,ny - 1):
                            if maps[nx + 1][ny] == 0 and maps[nx][ny - 1] == 0:
                                tmp = False
                        if tmp:  # 교차하는 절벽이 없으면
                            if (cnt + 1) % m == 0:
                                t = cnt + 1
                            else:
                                t = cnt + (m - cnt % m)
                            if t < d.get((nx, ny, True), INF):
                                q.append((nx, ny, t, True, True))
                                d[(nx, ny, True)] = t

n, m = map(int, input().split())
maps = [
    list(map(int, input().split())) 
    for _ in range(n)
] 
bfs()
print(answer) 