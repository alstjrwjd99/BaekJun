import sys
input = sys.stdin.readline

S = input().strip()

answer = ''
stack= ''
is_safe = False

def remove_signal(stack):
    return stack and stack[0] == '>'

def add_reverse_stack(answer, stack) :
    answer += stack[::-1]
    return answer, ''

for idx, char in enumerate(S):
    if char == '<':
        if remove_signal(stack) : stack = stack[1:]
        answer, stack = add_reverse_stack(answer, stack)
        is_safe = True
    elif char == '>':
        answer += char
        is_safe = False
    
    if is_safe :
        answer += char
    else :
        if char == ' ':
            if remove_signal(stack) : stack = stack[1:]
            answer, stack = add_reverse_stack(answer, stack)
            answer += ' '
        else :
            stack += char
            
if remove_signal(stack) : stack = stack[1:]
if stack and stack[-1] != '>' : answer += stack[::-1]
print(answer)