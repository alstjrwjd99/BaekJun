import heapq
from collections import defaultdict

def dijkstra(n, graph, start):
    distance = [float('inf') for _ in range(n)]
    distance[start] = 0
    hq = [(0, start)]
    
    while hq:
        cost, node = heapq.heappop(hq)
        
        if distance[node] < cost:
            continue
        
        for new_node, new_cost in graph[node]:
            sum_cost = cost + new_cost
            
            if distance[new_node] > sum_cost:
                distance[new_node] = sum_cost
                heapq.heappush(hq, (sum_cost, new_node))
    
    return distance

def solution(n, s, a, b, fares):
    # 그래프 초기화
    graph = defaultdict(list)
    
    # 노드 범위 확인 및 그래프 구성
    for fare in fares:
        u, v, cost = fare
        graph[u-1].append((v-1, cost))
        graph[v-1].append((u-1, cost))  # 그래프가 양방향일 경우
    
    # 다익스트라로 시작 노드에서의 최단 거리 계산
    dist_from_s = dijkstra(n, graph, s-1)
    
    # 결과 계산
    answer = float('inf')
    for i in range(n):
        # i에서 a와 b까지의 거리 계산
        dist_from_i = dijkstra(n, graph, i)
        total_cost = dist_from_i[a-1] + dist_from_i[b-1] + dist_from_s[i]
        answer = min(answer, total_cost)
    
    return answer