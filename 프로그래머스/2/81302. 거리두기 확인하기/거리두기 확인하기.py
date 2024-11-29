def solution(places):
    answer = [1] * 5
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

    def in_range(x, y):
        return 0 <= x < 5 and 0 <= y < 5

    def bfs(place, i, j):
        queue = [(i, j, 0)]  # (x, y, distance)
        visited = set([(i, j)])

        while queue:
            x, y, dist = queue.pop(0)
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if in_range(nx, ny) and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    if place[nx][ny] == 'P':  # 다른 사람 발견
                        if dist < 2:  # 거리 2 이내
                            return True
                    elif place[nx][ny] == 'O':  # 빈 테이블
                        if dist < 1:  # 거리 증가 가능
                            queue.append((nx, ny, dist + 1))
        return False

    for idx, place in enumerate(places):
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':  # 사람 위치에서 탐색 시작
                    if bfs(place, i, j):  # 거리두기 위반 확인
                        answer[idx] = 0
                        break  # 위반이 확인되면 더 이상 탐색하지 않음
            if answer[idx] == 0:
                break

    return answer