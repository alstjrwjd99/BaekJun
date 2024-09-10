import sys
input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# Direction vectors: 0 -> right, 1 -> down, 2 -> diagonal
dx = [0, 1, 1]
dy = [1, 0, 1]

# DP table to store the number of ways to reach each cell in each direction
# dp[x][y][dir] means the number of ways to reach (x, y) with the pipe in 'dir' orientation
dp = [[[0]*3 for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1  # The initial horizontal pipe from (0, 0) to (0, 1)

for x in range(N):
    for y in range(N):
        for direction in range(3):
            if dp[x][y][direction] == 0 or grid[x][y] == 1:
                continue
            
            # Move horizontally (to the right)
            if direction == 0 or direction == 2:  # If it's horizontal or diagonal
                nx, ny = x, y + 1
                if ny < N and grid[nx][ny] == 0:
                    dp[nx][ny][0] += dp[x][y][direction]
            
            # Move vertically (down)
            if direction == 1 or direction == 2:  # If it's vertical or diagonal
                nx, ny = x + 1, y
                if nx < N and grid[nx][ny] == 0:
                    dp[nx][ny][1] += dp[x][y][direction]
            
            # Move diagonally
            if direction == 0 or direction == 1 or direction == 2:
                nx, ny = x + 1, y + 1
                if nx < N and ny < N and grid[nx][ny] == 0 and grid[x+1][y] == 0 and grid[x][y+1] == 0:
                    dp[nx][ny][2] += dp[x][y][direction]

# The answer is the sum of all possible ways to reach the bottom-right corner in any direction
print(dp[N-1][N-1][0] + dp[N-1][N-1][1] + dp[N-1][N-1][2])