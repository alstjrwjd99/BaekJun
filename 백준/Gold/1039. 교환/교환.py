import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
n_str = str(n)
length = len(n_str)

# BFS를 위한 큐 초기화
queue = deque([(n_str, 0)])
visited = set()
visited.add((n_str, 0))
max_result = -1

while queue:
    current, swaps = queue.popleft()
    
    if swaps == k:
        max_result = max(max_result, int(current))
        continue

    for i in range(length):
        for j in range(i + 1, length):
            # 첫 번째 자리가 0이 되는 스왑은 무시
            if i == 0 and current[j] == '0':
                continue
            
            # 스왑
            new_current = list(current)
            new_current[i], new_current[j] = new_current[j], new_current[i]
            new_str = ''.join(new_current)
            
            if (new_str, swaps + 1) not in visited:
                visited.add((new_str, swaps + 1))
                queue.append((new_str, swaps + 1))

# 결과 출력
print(max_result)