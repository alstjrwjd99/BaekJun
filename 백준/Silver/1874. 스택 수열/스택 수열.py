import sys
input = sys.stdin.readline

n = int(input())
goal = [int(input()) for _ in range (n)]

stack = []
made = []
pointer = 0
answer = []
for i in range (1,n+1):
    stack.append(i)
    answer.append('+')
    while stack and stack[-1] == goal[pointer]:
        made.append(stack.pop())
        answer.append('-')
        pointer += 1
if made == goal:
    for ans in answer:
        print(ans)
else:
    print('NO')