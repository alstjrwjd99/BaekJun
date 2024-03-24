import heapq
import sys
input = sys.stdin.readline

n = int(input())
plus = []
minus = []
for _ in range (n):
  tmp = int(input())
  if tmp < 0 :
    heapq.heappush(minus,(-1)*tmp)
  elif tmp > 0 :
    heapq.heappush(plus, tmp)
  else :
    if minus:
      if plus:
        if minus[0] <= plus[0]:
          print((-1) * heapq.heappop(minus))
        else:
          print(heapq.heappop(plus))
      else:
        print(-heapq.heappop(minus))
    elif plus:
      print(heapq.heappop(plus))
    else:
      print(0)