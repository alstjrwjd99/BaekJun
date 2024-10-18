from collections import deque, defaultdict

def solution(n, wires):
    answer = float('inf')
    
    def find(wires):
        visited = set()
        graph = defaultdict(list)
        group = []
        
        for w,i in wires :
            graph[w].append(i)
            graph[i].append(w)
        
        def bfs(i):
            queue = deque([i])
            visited.add(i)
            tmp = [i]
            while queue:
                node= queue.popleft()
                for nex in graph[node]:
                    if nex not in visited:
                        queue.append(nex)
                        visited.add(nex)
                        tmp.append(nex)
            return len(tmp)
            
        
        for i in range (1,n+1):
            if i not in visited :
                group.append(bfs(i))
            
        return abs(group[0] - group[1])
        
    for i in range (len(wires)):
        answer = min(answer,find(wires[:i] + wires[i+1:]))
    return answer