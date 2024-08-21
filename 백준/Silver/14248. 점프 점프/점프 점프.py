import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
doldari = list(map(int,input().split()))
start = int(input())
queue = deque([start-1])
visited = set([start-1])

def in_range (x):
    return 0<= x < n

while queue:
    dol = queue.popleft()
    jump = doldari[dol]
    for will_move in (dol + jump , dol - jump ):
        if in_range(will_move) :
            queue.append(will_move)
            visited.add(will_move)
print(len(visited))