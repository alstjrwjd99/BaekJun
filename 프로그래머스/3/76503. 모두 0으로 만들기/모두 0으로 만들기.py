import sys
sys.setrecursionlimit(300000)
from collections import defaultdict

def solution(a, edges):
    if sum(a) != 0: return -1

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * len(a)
    answer = 0

    def dfs(node):
        nonlocal answer
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                child_sum = dfs(neighbor)
                answer += abs(child_sum)  
                a[node] += child_sum
        return a[node]

    for i in range(len(a)):
        if not visited[i]:
            dfs(i)
    return answer