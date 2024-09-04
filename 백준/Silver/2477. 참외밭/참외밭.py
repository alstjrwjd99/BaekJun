import sys
input = sys.stdin.readline

n = int(input())
cham_whys = [tuple(map(int, input().split())) for _ in range(6)]

max_row,max_col = -1e9,-1e9
# 큰 사각형의 너비와 높이 구하기
for direct, length in cham_whys:
    if direct >= 3:
        max_row = max(max_row,length)
    else:
        max_col = max(max_col,length)

# 작은 사각형의 너비와 높이 구하기
for i in range(6):
    if cham_whys[i][1] == max_row:
        small_row = cham_whys[(i + 3) % 6][1]
    if cham_whys[i][1] == max_col:
        small_col = cham_whys[(i + 3) % 6][1]

print((max_row * max_col - small_row * small_col) * n)