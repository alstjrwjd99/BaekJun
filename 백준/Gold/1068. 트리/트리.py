import sys
input = sys.stdin.readline

from collections import deque

n = int(input()) 
nodes = list(map(int, input().split()))
del_node = int(input())

def del_tree(s_node):
    queue = deque([s_node])    
    while queue:
        nd = queue.popleft()
        for n in tree[nd]:
            queue.append(n)
        tree[nd] = []
        
def leef_node(del_node,root):
    if del_node == root:
        return 0
    queue = deque([root])    
    leaf = 0
    while queue:
        nd = queue.popleft()
        if del_node in tree[nd]:
            tree[nd].remove(del_node)
        if not tree[nd]:
            leaf += 1
        else :
            for n in tree[nd]:
                queue.append(n)
    return leaf

tree = {i:[] for i in range (n)}
root = 0
for idx,node in enumerate(nodes):
    if node == -1:
        root = idx
    else :
        tree[node].append(idx)

del_tree(del_node)
print(leef_node(del_node,root))