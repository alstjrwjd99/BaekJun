import sys
input = sys.stdin.read

# 입력 받기
stories = input().splitlines()

for story in stories:
    if story == '.':  # 종료 조건
        break

    stack = []
    balanced = True  # 괄호의 균형이 맞는지 확인

    for char in story:
        if char == '[':
            stack.append('[')
        elif char == '(':
            stack.append('(')
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                balanced = False
                break
        elif char == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                balanced = False
                break

    # 스택이 비어 있고 balanced가 True이면 "yes", 아니면 "no"
    if balanced and not stack:
        print('yes')
    else:
        print('no')