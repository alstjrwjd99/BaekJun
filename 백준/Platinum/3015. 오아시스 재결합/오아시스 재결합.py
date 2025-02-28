import sys
input = sys.stdin.readline

n = int(input())
people = [int(input()) for _ in range(n)]

stack = []
answer = 0

for p in people:
    count = 1
    while stack and stack[-1][0] < p:
        answer += stack[-1][1]
        stack.pop()
        
    if stack and stack[-1][0] == p:
        cnt = stack[-1][1]
        stack.pop()
        answer += cnt 
        if stack:
            answer += 1
        count = cnt + 1
    else:
        if stack:
            answer += 1
    stack.append((p, count))

print(answer)