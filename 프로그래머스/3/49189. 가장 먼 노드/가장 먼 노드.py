from collections import defaultdict, deque

def solution(n, edge):
    # 인접 리스트로 그래프 생성
    graph = defaultdict(list)
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)
    
    # BFS를 위한 큐와 방문 집합
    queue = deque([(1, 0)])
    visited = set([1])
    distances = defaultdict(list)
    
    while queue:
        node, cnt = queue.popleft()
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, cnt + 1))
                visited.add(neighbor)
                distances[cnt + 1].append(neighbor)
    
    # 가장 먼 거리의 노드 개수 반환
    answer = len(distances[max(distances.keys())])

    return answer