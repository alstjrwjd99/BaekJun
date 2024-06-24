from copy import deepcopy
import sys
input = sys.stdin.readline
N,M = list(map(int,input().split()))

cctv = []
modes = [[], 
         [[0], [1], [2], [3]], 
         [[0, 2], [1, 3]],
         [[0, 1], [1, 2], [2, 3], [0, 3]],
         [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]], 
         [[0, 1, 2, 3]]]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
office = []

for i in range(N):
    tmp = list(map(int,input().split()))
    for j in range (M):
        if tmp[j] in (1,2,3,4,5):
            cctv.append((tmp[j],i,j))
    office.append(tmp)

def in_range(x,y):
    return 0<=x<N and 0<=y<M

def range_cctv(office, mode, x,y):
    for m in mode:  
        nx, ny = x, y
        while (in_range(nx,ny) and office[nx][ny] != 6):
            if office[nx][ny] in [1,2,3,4,5]:
                nx += dx[m]
                ny += dy[m]
            else :
                office[nx][ny] = '#'             
                nx += dx[m]
                ny += dy[m]
            
             
def dfs(depth, maps):
  global ans
  if depth == len(cctv):
    cnt = 0
    for i in range(N):
      cnt += maps[i].count(0)
    ans = min(ans, cnt)
    return

  temp = deepcopy(maps)
  cctv_num, x, y = cctv[depth]
  for mode in modes[cctv_num]: 
    range_cctv(temp, mode, x, y)
    dfs(depth + 1, temp)
    temp = deepcopy(maps)

ans = int(1e9)
dfs(0, office)
print(ans)
