import sys
import heapq

input = sys.stdin.readline

n = int(input())
tasks = []

for _ in range(n):
    deadline, cup_ramen = map(int, input().split())
    tasks.append((deadline, cup_ramen))
    
tasks.sort()

min_heap = []
for deadline, cup_ramen in tasks:
    heapq.heappush(min_heap, cup_ramen) 
    if len(min_heap) > deadline: 
        heapq.heappop(min_heap)  
print(sum(min_heap))