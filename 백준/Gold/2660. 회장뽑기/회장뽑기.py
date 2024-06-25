import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
relations = {i: set() for i in range(1, n+1)}

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    relations[a].add(b)
    relations[b].add(a)

def bfs(start):
    distances = [-1] * (n + 1)
    distances[start] = 0
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        for friend in relations[current]:
            if distances[friend] == -1:
                distances[friend] = distances[current] + 1
                queue.append(friend)
    
    return max(distances[1:])

scores = []
min_score = float('inf')

for i in range(1, n+1):
    score = bfs(i)
    scores.append((score, i))
    min_score = min(min_score, score)

candidates = sorted([i for score, i in scores if score == min_score])

print(min_score, len(candidates))
print(' '.join(map(str, candidates)))