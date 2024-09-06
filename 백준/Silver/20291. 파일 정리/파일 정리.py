import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
treasure = defaultdict(int)

for _ in range(N):
    file_name, extend_name = input().strip().split('.')
    treasure[extend_name] += 1

sort_key = sorted(treasure.keys())
for tre in sort_key:
    print(tre, treasure[tre])