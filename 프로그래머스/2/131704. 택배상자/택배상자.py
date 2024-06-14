'''
들어오는 숫자가 order이랑 같으면 빼고
다르면 stack에 넣고
'''
def solution(order):
    answer = 0
    stack = [0]
    pointer = 0
    for i in range (1, len(order)+1):
        if order[pointer] != stack[-1]:
            stack.append(i)
        while stack and pointer < len(order) and stack[-1] == order[pointer]:
            stack.pop()
            answer += 1
            pointer += 1
    return answer