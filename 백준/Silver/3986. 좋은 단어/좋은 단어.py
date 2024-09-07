import sys
input = sys.stdin.readline

n = int(input())
answer = 0
for _ in range (n):
    word = input().strip()
    stack = []
    cnt = 0
    for ab in word:
        if stack and stack[-1] == ab:
            stack.pop()
            cnt += 2
        else : stack.append(ab)
        
    if cnt == len(word):
        answer += 1
        
print(answer)