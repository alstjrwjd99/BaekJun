import sys
input = sys.stdin.readline

from collections import deque

N,M = list(map(int,input().split()))
rel = [
    list(map(int,input().split()))
    for _ in range (M)
]

answer = 0 

def find_related(h, relation):
    queue = deque([h])
    visited = set()
    while queue :
        man = queue.popleft()
        for friend in relation[man]:
            if friend not in visited:
                visited.add(friend)
                queue.append(friend)
    return visited

r_big = {i:[] for i in range (1,N+1)}
r_small =  {i:[] for i in range (1,N+1)}
    
for r in rel:
    r_big[r[0]].append(r[1])
    r_small[r[1]].append(r[0])
    
for i in range (1,N+1):
    left = find_related(i,r_small)
    right = find_related(i,r_big)
    find = left | right
    if len(find) == N-1:
        answer += 1
        
print(answer)