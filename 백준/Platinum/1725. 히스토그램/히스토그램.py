import sys
input = sys.stdin.readline

n = int(input())
heights = [ int(input()) for _ in range (n)]

stack = []
max_area = 0
heights.append(0)  # 마지막까지 남은 높이를 처리하기 위해

for i in range(len(heights)):
    while stack and heights[i] < heights[stack[-1]]:
        h = heights[stack.pop()]
        w = i if not stack else i - stack[-1] - 1
        max_area = max(max_area, h * w)
    stack.append(i)

heights.pop()  # 복구
print(max_area)

