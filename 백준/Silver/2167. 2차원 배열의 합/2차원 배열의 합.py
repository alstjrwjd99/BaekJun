size = list(map(int,input().split()))
arr = []
for _ in range (size[0]):
  arr.append(list(map(int,input().split())))
k = int(input())
for _ in range (k):
  answer = 0
  scope = list(map(int,input().split()))
  for i in range (scope[0]-1,scope[2]):
    answer += sum(arr[i][scope[1]-1:scope[3]])
  print(answer)