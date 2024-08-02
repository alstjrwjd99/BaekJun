import sys
from collections import defaultdict
sys.setrecursionlimit(100000)

def dfs(node):
    if not tree[node]:  # 리프 노드인 경우
        return 0
    times = []
    for child in tree[node]:
        times.append(dfs(child))
    times.sort(reverse=True)  # 많은 시간을 요하는 것부터 처리
    max_time = 0
    for idx, time in enumerate(times):
        max_time = max(max_time, time + idx + 1)
    return max_time

input = sys.stdin.readline
N = int(input().strip())
people = list(map(int, input().strip().split()))

tree = defaultdict(list)
for idx in range(1, N):
    tree[people[idx]].append(idx)

print(dfs(0))