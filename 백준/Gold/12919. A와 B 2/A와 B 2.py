S = input()
T = input()

def dfs():
    stack = [T]
    while stack:
        ab = stack.pop()
        if ab == S:
            return 1
        if ab == '':
            continue
        if ab[0] == 'B':
            stack.append(ab[1:][::-1])
        if ab[-1] == 'A':
            stack.append(ab[:-1])
    return 0

print(dfs())