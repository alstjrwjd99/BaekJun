import sys
input = sys.stdin.readline

n = int(input().strip())
arr = [[' '] * n for _ in range(n)]
STAR = '*'

def dfs(x, y, size):
    if size == 1:
        arr[x][y] = STAR
        return

    m = size // 3
    
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            dfs(x + i * m, y + j * m, m)

dfs(0, 0, n)
for row in arr:
    print(''.join(row))