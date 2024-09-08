import sys
input = sys.stdin.readline

row , col = map(int,input().split())
maps = [ list(map(int,input().split())) for _ in range (row)]

from collections import deque

def in_range(x,y) :
    return 0<=x<row and 0<= y< col

def bfs(i,j):
    queue =deque([(i,j)])
    visited = set([(i,j)])
    while queue:
        x,y = queue.popleft()
        for dx, dy in zip ((1,-1,0,0),(0,0,1,-1)):
            nx ,ny = x + dx , y + dy
            if in_range(nx,ny) and not (nx,ny) in visited:
                if maps[nx][ny] == 0:
                    queue.append((nx,ny))
                else :
                    maps[nx][ny] = 0
                visited.add((nx,ny))

def check_one():
    cnt = 0
    for i in range(row):
        for j in range(col):
            if maps[i][j] == 1 : cnt += 1
    return cnt

times = 0
second_answer = check_one()

while True:
    bfs(0,0)
    times += 1    
    cnt_one = check_one()
    if cnt_one == 0 :
        print(times)
        print(second_answer)
        break
    else : 
        second_answer = cnt_one