import sys
input = sys.stdin.readline

def correct_parentheses(parentheses):
    stack = []
    for par in parentheses:
        if par in '([':
            stack.append(par)
        elif par == ')':
            if not stack or stack[-1] == '[': 
                return 0
            elif stack[-1] == '(':
                stack.pop()
                stack.append(2) 
            else:
                temp = 0
                while stack and isinstance(stack[-1], int):
                    temp += stack.pop()
                if not stack or stack[-1] != '(':
                    return 0
                stack.pop()
                stack.append(temp * 2) 
        elif par == ']':
            if not stack or stack[-1] == '(':
                return 0
            elif stack[-1] == '[':
                stack.pop()
                stack.append(3)
            else:
                temp = 0
                while stack and isinstance(stack[-1], int):
                    temp += stack.pop()
                if not stack or stack[-1] != '[':
                    return 0
                stack.pop()
                stack.append(temp * 3) 
    result = 0
    for s in stack:
        if isinstance(s, int):
            result += s
        else: 
            return 0
    return result

parentheses = input().strip()
print(correct_parentheses(parentheses))