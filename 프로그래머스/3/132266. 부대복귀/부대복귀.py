from collections import deque

def solution(n, roads, sources, destination):

    visit = [-1]*(n+1)
    graph = [[] for _ in range(n+1)]
    for s, e in roads:
        graph[s].append(e)
        graph[e].append(s)

    Q = deque([destination])
    visit[destination] = 0
    while Q:
        now = Q.popleft()

        for node in graph[now]:
            if visit[node] == -1:
                visit[node] = visit[now]+1
                Q.append(node)

    return [visit[i] for i in sources]