import sys
input = sys.stdin.readline
from collections import defaultdict, deque

n, q = map(int, input().split())

usado = defaultdict(list)

for _ in range(n-1):
    u, v, r = map(int, input().split())
    usado[u].append((v, r))
    usado[v].append((u, r))

for _ in range(q):
    k, v = map(int, input().split())
    queue = deque([(v, float('inf'))])
    visited = set([v])
    answer = 0
    
    while queue:
        node, how_many_usa = queue.popleft()
        
        for recommend, relation in usado[node]:
            if recommend not in visited and relation >= k:
                visited.add(recommend)
                queue.append((recommend, min(how_many_usa, relation)))
                answer += 1

    print(answer)