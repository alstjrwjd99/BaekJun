import heapq
from collections import defaultdict

def solution(n, paths, gates, summits):
    graph = defaultdict(list)
    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))
    
    summits = set(summits)
    intensity = [float('inf')] * (n + 1)
    
    pq = [] 
    for gate in gates:
        heapq.heappush(pq, (0, gate))
        intensity[gate] = 0
    
    while pq:
        curr_intensity, node = heapq.heappop(pq)
        
        # 현재 노드가 산봉우리라면 더 이상 진행할 필요 없음
        if node in summits:
            continue
        
        if curr_intensity > intensity[node]:
            continue
        
        # 인접 노드 탐색
        for next_node, weight in graph[node]:
            max_intensity = max(curr_intensity, weight)
            if max_intensity < intensity[next_node]:
                intensity[next_node] = max_intensity
                heapq.heappush(pq, (max_intensity, next_node))
    
    answer = [0, float('inf')]
    for summit in sorted(summits):
        if intensity[summit] < answer[1]:
            answer = [summit, intensity[summit]]
            
    return answer