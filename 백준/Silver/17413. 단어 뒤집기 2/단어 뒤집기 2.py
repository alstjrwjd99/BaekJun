import sys
input = sys.stdin.readline

S = input().strip()

answer = ''
stack= ''
is_safe = False

for idx, char in enumerate(S):
    if char == '<':
        if stack and stack[0] == '>': stack = stack[1:]
        answer += stack[::-1]
        stack = ''
        is_safe = True
    elif char == '>':
        answer += char
        is_safe = False
    
    if is_safe :
        answer += char
    else :
        if char == ' ':
            if stack and stack[0] == '>': stack = stack[1:]
            answer += stack[::-1] + ' '
            stack = ''
        else :
            stack += char
if stack and stack[0] == '>': stack = stack[1:]
if stack and stack[-1] != '>' : answer += stack[::-1]
print(answer)
