from collections import deque

def solution(grid):
    n, m = len(grid), len(grid[0])
    visCount = -1
    visited = [[[ -1 for _ in range(2)] for _ in range(m)] for _ in range(n)]

    # 다음 가능한 이동 후보 반환
    def getNexts(i, j, k):
        nexts = []
        flag = grid[i][j]
        if flag == 1:  # '/'
            if k == 0:
                if j != 0:
                    nexts.append((i, j - 1, 1))
                if i != 0:
                    aFlag = grid[i - 1][j]
                    if aFlag == 1:
                        nexts.append((i - 1, j, 1))
                    else:
                        nexts.append((i - 1, j, 0))
            else:
                if j != m - 1:
                    nexts.append((i, j + 1, 0))
                if i != n - 1:
                    aFlag = grid[i + 1][j]
                    if aFlag == 1:
                        nexts.append((i + 1, j, 0))
                    else:
                        nexts.append((i + 1, j, 1))
        else:  # '\'
            if k == 0:
                if j != 0:
                    nexts.append((i, j - 1, 1))
                if i != n - 1:
                    aFlag = grid[i + 1][j]
                    if aFlag == 1:
                        nexts.append((i + 1, j, 0))
                    else:
                        nexts.append((i + 1, j, 1))
            else:
                if j != m - 1:
                    nexts.append((i, j + 1, 0))
                if i != 0:
                    aFlag = grid[i - 1][j]
                    if aFlag == 1:
                        nexts.append((i - 1, j, 1))
                    else:
                        nexts.append((i - 1, j, 0))
        return nexts

    # 투포인터로 최대 길이 계산
    def calculate(merged, isCycle):
        if not merged:
            return 0
        limit = len(merged)
        dupCheckSet = set()
        isDupExist = any(el in dupCheckSet or dupCheckSet.add(el) for el in merged)
        if isDupExist:
            limit -= 1

        if isCycle:
            merged = merged + merged

        left = 0
        memo = {}
        dupCounts = 0
        ret = 0

        def addMemo(el):
            nonlocal dupCounts
            if el not in memo:
                memo[el] = 1
            else:
                memo[el] += 1
                if memo[el] == 2:
                    dupCounts += 1

        def removeMemo(el):
            nonlocal dupCounts
            memo[el] -= 1
            if memo[el] == 1:
                dupCounts -= 1
            if memo[el] == 0:
                del memo[el]

        for right in range(len(merged)):
            addMemo(merged[right])
            while dupCounts >= 1:
                removeMemo(merged[left])
                left += 1
            ret = max(ret, right - left + 1)

        return min(limit, ret)

    # BFS 탐색
    def go(i, j, k):
        acc = []
        if visited[i][j][k] == visCount:
            return acc
        key = i * m + j
        acc.append(key)
        queue = deque([(i, j, k)])
        visited[i][j][k] = visCount
        while queue:
            newQueue = deque()
            while queue:
                x, y, z = queue.popleft()
                for nx, ny, nz in getNexts(x, y, z):
                    if visited[nx][ny][nz] != visCount:
                        acc.append(nx * m + ny)
                        newQueue.append((nx, ny, nz))
                        visited[nx][ny][nz] = visCount
            queue = newQueue
        return acc

    # 각 칸에 대해 탐색 시작
    def check(i, j, k):
        nonlocal visCount
        nexts = getNexts(i, j, k)
        visCount += 1
        visited[i][j][k] = visCount
        if not nexts:
            return 1
        results = [go(x, y, z) for (x, y, z) in nexts]
        isCycle = len(results) == 2 and len(results[1]) == 0
        merged = list(reversed(results[0])) + [i * m + j]
        if len(results) == 2:
            merged.extend(results[1])
        return calculate(merged, isCycle)

    res = 0
    for i in range(n):
        for j in range(m):
            for k in range(2):
                if visited[i][j][k] == -1:
                    res = max(res, check(i, j, k))
    return res