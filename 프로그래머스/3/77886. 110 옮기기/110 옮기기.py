def solution(s):
    def reorder(x):
        count_110 = 0
        stack = []

        for char in x:
            stack.append(char)
            if len(stack) >= 3 and stack[-3:] == ['1', '1', '0']:
                stack.pop()
                stack.pop()
                stack.pop()
                count_110 += 1
                
        result = ''.join(stack)
        idx = result.rfind('0') + 1
        return result[:idx] + '110' * count_110 + result[idx:]

    return [reorder(x) for x in s]