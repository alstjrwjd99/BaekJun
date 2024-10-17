def solution(s):
    answer = 0
    def is_correct(string):
        stack = []
        pairs = {'[':']', '(':')', '{':'}'}
        for st in string :
            if st in pairs:
                stack.append(st)
            else : 
                if stack and pairs[stack[-1]] == st:
                    stack.pop()
                else : return False
        if stack : return False
        return True
        
    for i in range (len(s)):
        if is_correct(s[i:] + s[:i]) : answer += 1
    return answer

