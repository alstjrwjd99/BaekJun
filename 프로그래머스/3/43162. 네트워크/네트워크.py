from collections import deque

def solution(n, computers):
    answer = 0
    queue = deque([])
    visited = set()
    
    def bfs(start):
        queue.append(start)
        while queue:
            node = queue.popleft()
            for idx, connect in enumerate(computers[node]):
                if connect == 1 and idx not in visited:
                    queue.append(idx)
                    visited.add(idx)
    
    for i in range (n):
        if i not in visited:
            bfs(i)
            answer += 1
                
    return answer