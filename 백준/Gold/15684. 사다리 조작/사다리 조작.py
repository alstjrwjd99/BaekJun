import sys
input = sys.stdin.readline

n, m, h = map(int, input().split())
ladder = [[False] * (n + 1) for _ in range(h + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    ladder[a][b] = True

def check(ladder):
    for i in range(1, n + 1):
        start = i
        for j in range(h + 1):
            if start < n and ladder[j][start]:
                start += 1
            elif start > 0 and ladder[j][start - 1]:
                start -= 1
        if i != start:
            return False
    return True

answer = 4 

def dfs(start, cnt, limit):
    global answer
    if cnt >= answer:
        return False
    if check(ladder):
        answer = cnt
        return True
    if cnt == limit:
        return False
    for pos in range(start, h * (n - 1)):
        r = pos // (n - 1) + 1
        c = pos % (n - 1) + 1
        if not ladder[r][c] and not ladder[r][c - 1] and not ladder[r][c + 1]:
            ladder[r][c] = True
            if dfs(pos + 1, cnt + 1, limit):
                return True
            ladder[r][c] = False
    return False

if check(ladder):
    print(0)
else:
    result = -1
    for limit in range(1, 4):
        if dfs(0, 0, limit):
            result = limit
            break
    print(result)