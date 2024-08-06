
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
#전 딕셔너리 형태로 작성을 하는것을 좋아한답니다
#근데 굳이? ㅋㅋ
graph = [input().rstrip() for _ in range(n)]
two_friend_dict = {i:set() for i in range(n)}

def bfs(start_node):
    q = deque([(start_node,0)]) # 현재노드, 현재 depth
    while q:
        # print(q)
        now_node, now_depth = q.popleft()
        if now_depth<2:
            for nxt_node,c in enumerate(graph[now_node]):
                if nxt_node == start_node :
                    continue
                if c=="Y" and nxt_node not in two_friend_dict[start_node]:
                    two_friend_dict[start_node].add(nxt_node)
                    q.append((nxt_node, now_depth+1))
        # print(two_friend_dict)

    return len(two_friend_dict[start_node])

answer = 0
for i in range(n):
    answer = max(answer, bfs(i))
print(answer)
