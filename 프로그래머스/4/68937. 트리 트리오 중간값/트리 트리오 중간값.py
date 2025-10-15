'''
Y자 모양이 포인트
중앙에서부터 거리가 a,b,c가 있다고 하면 ( a > b > c) a+b, a+c, b+c 의 중간값의 최대를 구해야함
그러면 a+c 의 최대가 될 것
1. 임의의 점 1번 잡고 bfs -> 가장 먼 점과 거리를 return
2. 그 점에서 또 bfs -> 여기서도 가장 먼 점과 거리를 return
3. 2번 한번더
'''
from collections import deque, defaultdict

def solution(n, edges):
    answer = 0
    graph = defaultdict(list)
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    def bfs(start):
        queue = deque([start])
        dist = [-1] * (n + 1)
        dist[start] = 0
        far = start
        while queue:
            v = queue.popleft()
            if dist[v] > dist[far]:
                far = v
            for w in graph[v]:
                if dist[w] == -1:
                    dist[w] = dist[v] + 1
                    queue.append(w)
        return far, dist
    
    s, _ = bfs(1)
    t, dist_s = bfs(s)
    D = dist_s[t]
    _, dist_t = bfs(t)
    
    A = {v for v, d in enumerate(dist_s) if d == D}
    B = {v for v, d in enumerate(dist_t) if d == D}
    cnt = len(A | B)
    answer = D if cnt >= 3 else D-1
    return answer