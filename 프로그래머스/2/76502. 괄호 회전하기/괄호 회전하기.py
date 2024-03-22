def solution(s):
    answer = 0
    n = len(s)
    # 올바른 괄호인지 파악하는 함수 작성
    # 문자열 회전하는 코드 작성
    def isParth(parth):
        stack = []
        stack.append(parth[0])
        for i in range (1,len(parth)):
            if len(stack) == 0:
                stack.append(parth[i])
            else :
                if stack[-1] == '[' and parth[i] == ']':
                    stack.pop()
                elif stack[-1] == '(' and parth[i] == ')':
                    stack.pop()
                elif stack[-1] == '{' and parth[i] == '}':
                    stack.pop()
                else :
                    stack.append(parth[i])
        if len(stack) == 0:
            return True
        else : return False
    for i in range (n):
        s = s[1:] + s[0]
        if isParth(s) :
            answer += 1
    
    return answer