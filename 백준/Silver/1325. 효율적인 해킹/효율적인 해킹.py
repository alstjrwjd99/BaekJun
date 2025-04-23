import sys
input = sys.stdin.readline

from collections import deque, defaultdict

n,m = map(int, input().split())
relation = defaultdict(list)

for i in range (m):
    a,b = map(int, input().split())
    relation[b].append(a)

def bfs(start):
    queue = deque([start])
    visited = set([start])
    cnt = 0
    
    while queue :
        computer = queue.popleft()
        for trust in relation[computer]:
            if (trust not in visited):
                cnt += 1
                queue.append(trust)
                visited.add(trust)
    return cnt

max_int = 0
answer = []

for i in range (1,n+1):
    count = bfs(i)
    if (max_int < count):
        answer = [i]
        max_int = count
    elif (max_int == count) :
        answer.append(i)

print(*answer)