from collections import deque

def solution(grid):
    n = len(grid)
    m = len(grid[0])
    G = [row.encode() for row in grid]

    WALL = ord('#')
    BALL = ord('o')
    SNOW = ord('.')

    starts = []
    for y, row in enumerate(G):
        for x, b in enumerate(row):
            if b == BALL:
                starts.append(y * m + x)

    s0, s1 = starts
    N = n * m

    been0 = bytearray(N)
    been1 = bytearray(N)

    snowball_distance = N + 1
    is_case2 = False
    dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

    def bfs(start, been, other, other_been=None):
        nonlocal snowball_distance, is_case2
        q = deque([(start, 0)])
        been[start] = 1
        three_dist = -1

        while q:
            idx, dis = q.popleft()
            y, x = divmod(idx, m)

            choices = 0
            for dx, dy in dirs:
                nx = x + dx
                ny = y + dy
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                cell = G[ny][nx]
                if cell == WALL:
                    continue

                choices += 1
                nidx = ny * m + nx

                if been[nidx]:
                    continue

                if nidx == other:  # 다른 눈덩이 시작 위치는 통과 불가(거리만 갱신)
                    nd = dis + 1
                    if nd < snowball_distance:
                        snowball_distance = nd
                    continue

                been[nidx] = 1
                q.append((nidx, dis + 1))

            if choices >= 3:
                if other_been is not None and other_been[idx] and G[y][x] == SNOW:
                    is_case2 = True
                if three_dist == -1:
                    three_dist = dis

        return three_dist

    three0 = bfs(s0, been0, s1)
    three1 = bfs(s1, been1, s0, been0)

    shared = a_only = b_only = 0
    for idx in range(N):
        y, x = divmod(idx, m)
        cell = G[y][x]
        if cell == WALL or cell == BALL:
            continue

        b0 = been0[idx]
        b1 = been1[idx]
        if b0 and b1:
            shared += 1
        elif b0:
            a_only += 1
        elif b1:
            b_only += 1

    def calculate(case_type, dist, shared_blocks, a_only_blocks, b_only_blocks, dis_to_threeway):
        ret = 0
        shared_local = shared_blocks
        total = shared_blocks + a_only_blocks + b_only_blocks

        start = dist - 1
        if start < 0:
            start = 0

        for i in range(start, total + 1):
            if case_type == 3 and i > shared_local + a_only_blocks + dis_to_threeway + 1:
                shared_local += 1

            if case_type == 2:
                ret += i // 2 + 1
            else:
                ret += min(i // 2 + 1, a_only_blocks + shared_local + 1)

            if case_type == 1 and i > b_only_blocks + shared_local:
                ret -= i - b_only_blocks - shared_local

        return ret

    # CASE 1: 양쪽 모두 갈림길 없음
    if three0 == -1 and three1 == -1:
        return calculate(1, snowball_distance, shared, min(a_only, b_only), max(a_only, b_only), 250001)

    # CASE 2(및 4): 공유영역에 갈림길이 있거나, 양쪽 모두 갈림길 있음
    if (three0 != -1 and three1 != -1) or is_case2:
        return calculate(2, snowball_distance, shared, a_only, b_only, 0)

    # CASE 3: 한쪽만 갈림길 있음 (a_only가 '외길' 쪽, b_only가 '갈림길' 쪽이 되도록 정렬)
    if three0 == -1:
        return calculate(3, snowball_distance, shared, a_only, b_only, three1)
    return calculate(3, snowball_distance, shared, b_only, a_only, three0)