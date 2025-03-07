import sys
input = sys.stdin.readline
from collections import deque

l,r,c = list(map(int,input().split()))
# x가 높이 
dxs, dys, dzs = (0,0,0,0,1,-1),(-1,0,1,0,0,0),(0,1,0,-1,0,0)

def in_range(x,y,z):
    return 0<=x<l and 0<=y<r and 0<=z<c

def solution(building):
    queue = deque()
    visited = set()
    
    for i in range (l):
        for j in range (r):
            for k in range (c):
                if building[i][j][k] == 'S' :
                    queue.append((i,j,k,1))
                    visited.add((i,j,k))
                    break
    
    while queue :
        x,y,z,cnt = queue.popleft()
        for dx,dy,dz in zip(dxs, dys, dzs):
            nx , ny , nz = x +dx, y + dy, z + dz
            if in_range(nx,ny,nz) and (nx,ny,nz) not in visited:
                if building[nx][ny][nz] == '.':
                    visited.add((nx,ny,nz))
                    queue.append((nx,ny,nz,cnt + 1))
                elif building[nx][ny][nz] == 'E':
                    return cnt
                
    return 0

while not (l == r == c == 0) :
    building = []

    for height in range (l):
        tmp = []
        for row in range (r) :
            line = list(input().strip())
            tmp.append(line)
        building.append(tmp)
        input()
    
    moved = solution(building)
    if moved == 0:
        print('Trapped!')
    else :
        print(f'Escaped in {moved} minute(s).')
    l,r,c = list(map(int,input().split()))