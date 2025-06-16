'''
뒤의 숫자가 더 크면 지우기
'''
def solution(number, k):
    stack = []
    for n in number :
        while stack and stack[-1] < int(n) and k > 0:
            stack.pop()
            k -= 1
        stack.append(int(n))
    while k > 0 :
        stack.remove(min(stack))
        k -= 1
    return ''.join(map(str,stack))