N,M,q = list(map(int,input().split()))
arr = []
qu = []
for i in range (N):
  arr.append(list(map(int,input().split())))
for i in range (q):
  qu.append(list(map(int,input().split())))
for qq in qu:
  if qq[0] == 0:
    arr[qq[1]][qq[2]] = qq[3]
  else :
    arr[qq[1]], arr[qq[2]] = arr[qq[2]], arr[qq[1]]
for a in arr:
  print(*a)