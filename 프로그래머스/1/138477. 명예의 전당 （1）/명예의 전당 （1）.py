def solution(k, score):
    answer = []
    stack = []
    for at in score:
        stack.append(at)
        mini = min(stack)
        if len(stack) > k:
            stack.remove(mini)
            mini = min(stack)
        answer.append(mini)
    return answer