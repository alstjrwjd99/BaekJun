import sys
sys.setrecursionlimit(1000000)
from collections import defaultdict

def solution(n, lighthouse):
    graph = defaultdict(list)
    for u, v in lighthouse:
        graph[u].append(v)
        graph[v].append(u)

    dp = [[0, 0] for _ in range(n + 1)] 
    visited = [False] * (n + 1)

    def dfs(node):
        visited[node] = True
        dp[node][0] = 0
        dp[node][1] = 1

        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
                dp[node][0] += dp[neighbor][1] 
                dp[node][1] += min(dp[neighbor][0], dp[neighbor][1]) 

    dfs(1)
    return min(dp[1][0], dp[1][1])