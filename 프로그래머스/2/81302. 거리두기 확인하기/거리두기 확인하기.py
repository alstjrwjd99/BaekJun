from collections import deque

def solution(places):
    answer = [1] * 5
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

    def in_range(x, y):
        return 0 <= x < 5 and 0 <= y < 5

    def bfs(place, i, j):
        queue = deque([(i, j, 0)])
        visited = set([(i, j)])

        while queue:
            x, y, dist = queue.popleft()
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if in_range(nx, ny) and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    if place[nx][ny] == 'P':
                        if dist < 2:
                            return True
                    elif place[nx][ny] == 'O':
                        if dist < 1:
                            queue.append((nx, ny, dist + 1))
        return False

    for idx, place in enumerate(places):
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if bfs(place, i, j):
                        answer[idx] = 0
                        break 
            if answer[idx] == 0:
                break

    return answer