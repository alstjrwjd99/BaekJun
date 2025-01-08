def solution(s):   
    def find_110(x):
        stack = []
        cnt_110 = 0
        
        for char in x:
            stack.append(char)
            if len(stack) >= 3 and stack[-3:] == ['1','1','0']:
                stack.pop()
                stack.pop()
                stack.pop()
                cnt_110 += 1
        
        new_x = ''.join(stack)
        idx = new_x.rfind('0') + 1
        return new_x[:idx] + '110' * cnt_110 + new_x[idx:]
        
        
    return [find_110(x) for x in s]