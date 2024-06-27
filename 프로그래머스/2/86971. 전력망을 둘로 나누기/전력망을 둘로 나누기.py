from collections import deque

def count_tree(n,graph):
    queue = deque([graph[0][0],graph[0][1]])
    visited = set()
    while queue:
        point = queue.popleft()
        for edge in graph:
            if edge[0] == point and edge[1] not in visited:
                queue.append(edge[1])
                visited.add(edge[1])
            elif edge[1] == point and edge[0] not in visited:
                queue.append(edge[0])
                visited.add(edge[0])
                
    return abs(n-len(visited)-len(visited))

def solution(n, wires):
    answer = n
    for i in range (n-1):
        seperated = wires[:i] + (wires[i+1:])
        answer = min(answer,count_tree(n,seperated))
    return answer