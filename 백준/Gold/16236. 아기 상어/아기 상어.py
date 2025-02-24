import sys
input = sys.stdin.readline

from collections import deque 

n = int(input())
place = [ list(map(int,input().split())) for _ in range (n)]
dxs, dys = [-1,0,1,0],[0,1,0,-1]
baby_shark = {
    'x' : 0, 'y' : 0 , 'size' : 2 , 'eat' : 0 
}
INF = float('inf')

for i in range (n):
    for j in range (n):
        if place[i][j] == 9 :
            baby_shark['x'] = i
            baby_shark['y'] = j
            break

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def find_smallest_fish(bs):
    i,j, current_size = bs['x'], bs['y'], bs['size']
    queue = deque([(i,j,0)])
    visited = set([(i,j)])
    smallest = [INF,INF,INF] # x,y, moved_cnt
    
    while queue:
        x,y,moved = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx , y + dy
            if in_range(nx,ny) and (nx,ny) not in visited:
                if place[nx][ny] < current_size:
                    queue.append((nx,ny,moved+1))
                    visited.add((nx,ny))
                    if place[nx][ny] != 0:
                        # 새로운 후보의 이동 거리는 moved+1
                        if moved+1 < smallest[2]:
                            smallest = [nx, ny, moved+1]
                        elif moved+1 == smallest[2]:
                            # 행 번호가 작거나, 행이 같다면 열 번호가 작은 경우 업데이트
                            if nx < smallest[0] or (nx == smallest[0] and ny < smallest[1]):
                                smallest = [nx, ny, moved+1]
                elif place[nx][ny] == current_size:
                    queue.append((nx,ny,moved + 1))
                    visited.add((nx,ny))    

    if smallest != [INF,INF,INF] :
        place[i][j] = 0
        place[smallest[0]][smallest[1]] = 9
    return smallest

answer = 0 
while True: 
    place_x, place_y , moved = find_smallest_fish(baby_shark)
    if (place_x != INF and place_y != INF):
        if baby_shark['eat'] + 1 == baby_shark['size'] :
            baby_shark['x'] = place_x
            baby_shark['y'] = place_y
            baby_shark['size'] += 1 
            baby_shark['eat'] = 0
        elif baby_shark['eat'] + 1 < baby_shark['size'] :
            baby_shark['x'] = place_x
            baby_shark['y'] = place_y
            baby_shark['eat'] += 1
            
        answer += moved
    else :
        break

print(answer)