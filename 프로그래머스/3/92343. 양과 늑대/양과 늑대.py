from collections import defaultdict

def solution(info, edges):
    global answer
    answer = 0
    tree = defaultdict(list)
    for u,v in edges :
        tree[u].append(v)
    
    def dfs(node, sheep, wolf, possible):
        global answer
        
        # 현재 양과 늑대 상태가 유효하지 않으면 중단
        if sheep <= wolf:
            return
    
        answer = max(answer, sheep)
        
        for nxt in possible:
            new_possible = possible.copy()
            new_possible.remove(nxt)
            new_possible.extend(tree[nxt])
            
            if info[nxt] == 0:
                dfs(nxt, sheep + 1, wolf, new_possible)
            else:
                dfs(nxt, sheep, wolf + 1, new_possible)
    
    dfs(0, 1, 0, tree[0])
    return answer