n,m = map(int,input().split())
tree = list(map(int,input().split()))
start,end = 1,max(tree)

while start <= end:
  get = 0
  mid = (start + end) // 2 
  for tr in tree :
    if tr > mid :
      get += (tr - mid)
  if get >= m:
    start = mid + 1
  else :
    end = mid - 1
print(end)