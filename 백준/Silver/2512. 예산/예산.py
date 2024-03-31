n = int(input())
require = list(map(int,input().split()))
budget = int(input())

start,end = 0,max(require)

while start <= end:
  tmp = 0
  mid = (start + end) // 2
  for req in require:
    if req <= mid:
      tmp += req
    else :
      tmp += mid
  if tmp > budget:
    end = mid - 1
  else :
    start = mid + 1
print(end)