from collections import deque

def solution(storage, requests):
    answer = 0
    n, m = len(storage), len(storage[0])
    dxs, dys = (0, 1, 0, -1), (1, 0, -1, 0)

    new_st = [[0] * (m + 2)]
    for i in range(n):
        new_st.append([0] + list(storage[i]) + [0])
    new_st.append([0] * (m + 2)) 

    def in_range(x, y):
        return 0 <= x < len(new_st) and 0 <= y < len(new_st[0])

    def check_side():
        queue = deque([(0, 0)])
        visited = set([(0, 0)])
        while queue:
            x, y = queue.popleft()
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if in_range(nx, ny) and (nx, ny) not in visited:
                    if new_st[nx][ny] == 0:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
                    elif new_st[nx][ny] == target:
                        new_st[nx][ny] = 0
                        visited.add((nx, ny))

    for req in requests:
        target = req[0]
        if len(req) == 1:
            check_side()
        elif len(req) == 2:
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    if new_st[i][j] == target:
                        new_st[i][j] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if new_st[i][j] != 0:
                answer += 1

    return answer