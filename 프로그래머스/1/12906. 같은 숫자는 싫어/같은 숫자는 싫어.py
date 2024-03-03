def solution(arr):
    stack = []
    stack.append(arr[0])
    for ar in arr :
        if stack[-1] != ar :
            stack.append(ar)
    return stack