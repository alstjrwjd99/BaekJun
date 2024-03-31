n,k = map(int,input().split())
num = []

for _ in range (n):
  num.append(int(input()))

start,end = 1, max(num)

while start <= end :
  mid = (start + end)//2
  lans = 0
  for i in num :
    lans += i // mid
  if lans >= k:
    start = mid + 1
  else :
    end = mid - 1
print(end)