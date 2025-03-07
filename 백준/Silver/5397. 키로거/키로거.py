import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    left = []
    right = []
    s = input().strip()
    for c in s:
        if c == '<':
            if left:
                right.append(left.pop())
        elif c == '>':
            if right:
                left.append(right.pop())
        elif c == '-':
            if left:
                left.pop()
        else:
            left.append(c)
    print(''.join(left + right[::-1]))