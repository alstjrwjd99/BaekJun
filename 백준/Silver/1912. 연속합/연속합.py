A = int(input())
numlist = list(map(int,input().split()))
for i in range (1,A):
  numlist[i] = max(numlist[i],numlist[i]+ numlist[i-1])

print(max(numlist))