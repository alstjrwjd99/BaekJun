import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range (n):
  iszero = int(input())
  if iszero == 0 :
    heapq.heappush(heap, iszero*(-1))
    print((-1)*heapq.heappop(heap))
  else :
  	heapq.heappush(heap, iszero*(-1))
