'''
1. 맨 밑에서 2 index찾기
2. 좌우 먼저 탐색 후 위로 탐색해서 길찾기
3. 마지막 y좌표 출력
'''
T = 10

dxs,dys= [0,0,-1],[1,-1,0]
for test_case in range(1, T+1):
    start = int(input())
    visited = set()
    grid = [
        list(map(int,input().split()))
        for _ in range (100)
    ]
    x = 99
    y = grid[99].index(2)
    visited.add((x,y))
    while x != 0:
        for dx,dy in zip(dxs,dys):
            nx = dx + x
            ny = dy + y
            if 0<=nx<100 and 0<=ny<100 and grid[nx][ny] == 1 and (nx,ny) not in visited:
                x = nx
                y = ny
                visited.add((nx,ny))
                break     

    print(f'#{start} {y}')
