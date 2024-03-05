n = int(input())
arr = []
for i in range (n):
  arr.append(int(input()))
arr.sort()
answer = []
for i in range (n):
  cnt = 0
  for j in range (arr[i],arr[i]+5) :
    if j not in arr:
      cnt += 1
  answer.append(cnt)
print(min(answer))