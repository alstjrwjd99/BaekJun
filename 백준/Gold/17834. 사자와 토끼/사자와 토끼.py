import sys
from collections import deque

input = sys.stdin.readline

def is_bipartite(graph, n):
    color = [-1] * (n + 1)
    
    def bfs(start):
        queue = deque([start])
        color[start] = 0
        
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False
        return True
    
    for i in range(1, n + 1):
        if color[i] == -1:
            if not bfs(i):
                return False, []
    
    set1 = [i for i in range(1, n + 1) if color[i] == 0]
    set2 = [i for i in range(1, n + 1) if color[i] == 1]
    return True, (set1, set2)

def count_unending_positions(n, bushes):
    graph = {i: [] for i in range(1, n + 1)}
    for u, v in bushes:
        graph[u].append(v)
        graph[v].append(u)
    
    bipartite, sets = is_bipartite(graph, n)
    if not bipartite:
        return 0
    
    set1, set2 = sets
    return len(set1) * len(set2) * 2

n, m = map(int, input().split())
bushes = [tuple(map(int, input().split())) for _ in range(m)]

print(count_unending_positions(n, bushes))