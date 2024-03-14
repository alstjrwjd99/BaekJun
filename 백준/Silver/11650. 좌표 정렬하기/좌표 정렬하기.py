n = int(input())
answer = []
for _ in range (n):
  answer.append(list(map(int,input().split())))
answer.sort(key = lambda x : (x[0],x[1]))
for a in answer :
  print(a[0],a[1])