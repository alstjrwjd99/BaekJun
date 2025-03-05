import sys
input = sys.stdin.readline

n = int(input())
A, B, C, D = [], [], [], []
for _ in range(n):
  a, b, c, d = map(int, input().split())
  A.append(a)
  B.append(b)
  C.append(c)
  D.append(d)

AB, CD = [], []
for i in range(n):
  for j in range(n):
    AB.append(A[i] + B[j])
    CD.append(C[i] + D[j])
AB.sort()
CD.sort()

start, end = 0, n**2-1
count = 0

while start < len(AB) and end >= 0:
  if AB[start] + CD[end] == 0:
    count_start, count_end = start + 1, end - 1
    
    while count_start < len(AB) and AB[start] == AB[count_start]:
      count_start += 1
      
    while count_end >= 0 and CD[end] == CD[count_end]:
      count_end -= 1
    
    count += (count_start - start) * (end - count_end)
    start, end = count_start, count_end
    
  elif AB[start] + CD[end] > 0:
    end -= 1
    
  else:
    start += 1
    
print(count)