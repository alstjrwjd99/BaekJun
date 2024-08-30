def divide(p):
    left,right,pointer = 0,0,0
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            pointer = i
            break
    u = p[:pointer+1]
    v = p[pointer+1:]
    return u,v

def is_correct(p):
    stack = []
    for i in p:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return True
    
def solution(p):
    answer = ''
    
    if p == '':
        return ''
    
    u,v = divide(p)
    if is_correct(u):
        answer += u
        temp = solution(v)
        if temp == '':
            return answer
        else:
            answer += temp
    else:
        tmp = '(' + solution(v) + ')'
        u = u[1:-1]
        for i in u:
            if i == '(':
                tmp += ')'
            else:
                tmp += '('
        return tmp
    
    return answer
    