'''
완전 탐색
한 점에서 4가지 방향으로 탐색 -> 10 ^ 6

현재 가려는 방향 cur_direct : [0,1]
S를 만난 경우 : [0,1] -> x,y

L을 만난 경우 : [-1,0] -> -y,x
R을 만난 경우 : [1,0]  -> y,x

처음 출발한 곳으로 돌아오면 끝

범위 벗어나는 경우 n -> 0 or -1 -> n-1

방문한 경로 체크

정렬해서 return
'''
def solution(grid):
    answer = []
    n, m = len(grid), len(grid[0])  # 그리드의 크기
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상, 우, 하, 좌
    visited = set()  # 방문한 (x, y, 방향)을 추적하기 위한 집합

    # 각 좌표에서 모든 방향으로 시뮬레이션 시작
    for i in range(n):
        for j in range(m):
            for d in range(4):  # 각 방향
                if (i, j, d) in visited:
                    continue

                length = 0
                x, y, direction = i, j, d

                # 탐색 시작
                while (x, y, direction) not in visited:
                    visited.add((x, y, direction))
                    length += 1

                    # 다음 위치 계산
                    dx, dy = directions[direction]
                    x, y = (x + dx) % n, (y + dy) % m

                    # 다음 방향 계산
                    if grid[x][y] == 'L':
                        direction = (direction - 1) % 4
                    elif grid[x][y] == 'R':
                        direction = (direction + 1) % 4

                if length > 0:
                    answer.append(length)

    return sorted(answer)