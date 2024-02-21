from collections import deque
n = int(input())
queue = deque([])
for i in range (1,n+1):
  queue.append(i)
while len(queue) != 1:
  ad = queue.popleft()
  add = queue.popleft()
  queue.append(add)
print(queue[0])