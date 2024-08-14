from collections import deque

def solution(n, edge):
    answer = [0] * (n+1)
    graph = {i:[] for i in range (1,n+1)}
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    queue = deque([(1,0)])
    visited = set([1])
    while queue:
        node,distance = queue.popleft()
        for next_node in graph[node]:
            if not next_node in visited:
                queue.append((next_node,distance+1))
                visited.add(next_node)
                # leaf node
                if graph[next_node]:
                    answer[next_node] = distance+1
    
    return answer.count(max(answer))                    