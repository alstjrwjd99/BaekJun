import sys
input = sys.stdin.readline

n = int(input())
heights = [ int(input()) for _ in range (n)]

stack = []
answer = 0
heights.append(0)

for i in range(n+1):
    while stack and heights[stack[-1]] > heights[i]:
        h = heights[stack.pop()]
        w = i if not stack else i - stack[-1] - 1
        answer = max(answer, w*h)
    stack.append(i)
print(answer)