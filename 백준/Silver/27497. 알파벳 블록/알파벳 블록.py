import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
dq = deque([])
is_front_last = []

for _ in range (n):
    command = input().split()
    if len(command) == 2:
        cmd , char = command[0], command[1]
        if cmd == '1':
            dq.append(char)
            is_front_last.append(False)
        elif cmd == '2':
            dq.appendleft(char)
            is_front_last.append(True)
    else : 
        if dq and is_front_last:
            if is_front_last.pop():
                dq.popleft()
            else :
                dq.pop()
        
if dq :
    print(''.join(dq))
else :print(0)