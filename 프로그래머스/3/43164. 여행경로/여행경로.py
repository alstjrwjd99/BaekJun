from collections import defaultdict

def solution(tickets):
    answer = []
    graph = defaultdict(list) 
    for u,v in sorted(tickets, reverse = True):
        graph[u].append(v)
    
    def dfs(node):
        while graph[node]:
            print(node)
            dfs(graph[node].pop())
        answer.append(node)
        
    dfs('ICN')
    return answer[::-1]