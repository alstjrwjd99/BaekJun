import sys
input = sys.stdin.readline

N,M = map(int,input().split())
Tg , Tb, X, b = map(int,input().split())

city = []
viruses = []

for i in range (N):
    tmp = list(input().split()[0])
    for j in range (M):
        if tmp[j] == '*':
            viruses.append((i,j))
    city.append(tmp)

dxs, dys = [-1,1,0,0],[0,0,1,-1]
building = {}

def in_range(x,y):
    return 0<=x<N and 0<=y<M

def expand(virus,t):
    for dx, dy in zip(dxs,dys):
        nx = virus[0] + dx
        ny = virus[1] + dy
        if in_range(nx,ny):
            if city[nx][ny] == '.':
                city[nx][ny] = '*'
                tmp_virus.append((nx,ny))
            elif city[nx][ny] == '#':
                # 건물 처리
                if t in building:
                    building[t].append((nx,ny))
                else :
                    building[t] = [(nx,ny)]
                city[nx][ny] = 'B'

for t in range (1,Tg+1):
    tmp_virus = []
    for virus in viruses:
        if city[virus[0]][virus[1]] == '*':
            expand((virus[0],virus[1]),t) 
    if (t-Tb) in building:
        for b in building[t-Tb]:
            city[b[0]][b[1]] = '*'
            tmp_virus.append((b[0],b[1]))
    viruses = tmp_virus

safe = False

for i in range(N):
    for j in range (M):
        if city[i][j] != '*':
            print(i+1,j+1)
            safe = True
if not safe:
    print(-1)