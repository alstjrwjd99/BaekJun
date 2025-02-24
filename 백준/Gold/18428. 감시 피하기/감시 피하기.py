import sys
input = sys.stdin.readline

n = int(input())
corridor = [list(input().split()) for _ in range(n)]

answer = "NO"

def check():
    for i in range(n):
        for j in range(n):
            if corridor[i][j] == 'T':
                for dx, dy in [(-1,0), (0,1), (1,0), (0,-1)]:
                    nx, ny = i + dx, j + dy
                    while 0 <= nx < n and 0 <= ny < n:
                        if corridor[nx][ny] == 'S':
                            return False
                        elif corridor[nx][ny] == 'O':
                            break
                        nx += dx
                        ny += dy
    return True

def dfs(start, cnt):
    global answer
    if cnt == 3:
        if check():
            answer = "YES"
            return True
        return False

    for i in range(start, n * n):
        r = i // n
        c = i % n
        if corridor[r][c] == 'X':
            corridor[r][c] = 'O'
            if dfs(i + 1, cnt + 1):
                return True
            corridor[r][c] = 'X'
    return False

dfs(0, 0)
print(answer)