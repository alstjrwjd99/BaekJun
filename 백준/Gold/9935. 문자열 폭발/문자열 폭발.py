import sys
input = sys.stdin.readline

seq = input().strip()
bomb = input().strip()
bomb_len = len(bomb)
stack = []

for s in seq:
    stack.append(s)
    if ''.join(stack[-bomb_len:]) == bomb:
        del stack[-bomb_len:]

if stack:
    print(''.join(stack))
else:
    print('FRULA')