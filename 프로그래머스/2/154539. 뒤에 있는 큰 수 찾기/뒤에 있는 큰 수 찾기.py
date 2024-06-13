'''
브루트포스는 시간초과
stack으로 풀어보자
'''
def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    for i in range (len(numbers)-1):
        stack.append((numbers[i],i))
        while stack and stack[-1][0] < numbers[i+1]:
                number,index = stack.pop()
                answer[index] = numbers[i+1]

    return answer