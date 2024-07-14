from collections import deque

def solution(n, results):
    answer = 0
    left = {i+1 : [] for i in range(n)}
    right = {i+1 : [] for i in range(n)}
    
    for result in results:
        left[result[0]].append(result[1])
        right[result[1]].append(result[0])
    
    def bfs(start,lr):
        queue = deque([start])
        visited =set()
        while queue:
            gwon = queue.popleft()
            for i in lr[gwon]:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)
        return visited
        
        
    for i in range(1,n+1):
        left_mem = bfs(i,left)
        right_mem = bfs(i,right)
        total = left_mem | right_mem
        if len(total) == n-1:
            answer += 1
    
    return answer