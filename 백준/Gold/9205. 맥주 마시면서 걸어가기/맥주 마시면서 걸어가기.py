from collections import deque
t = int(input())
for _ in range (t):
  answer = False
  convin = []
  queue = deque([])
  n = int(input())
  visited = [False] * n
  house = list(map(int,input().split()))
  queue.append(house)
  for _ in range (n):
    convin.append(list(map(int,input().split()))) 
  festival = list(map(int,input().split()))
  while queue:
    a = queue.popleft()
    if (abs(a[0]-festival[0]) + abs(a[1]-festival[1]) <= 1000):
      answer = True
      break
    for i,convi in enumerate (convin):
      if (abs(a[0]-convi[0]) + abs(a[1]-convi[1]) <= 1000) and not visited[i] :
        queue.append(convi)
        visited[i] = True
  if answer :
    print("happy")
  else :
    print("sad")
