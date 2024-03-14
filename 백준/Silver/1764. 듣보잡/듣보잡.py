n,m = map(int,input().split())
answer = []
name = set()
for _ in range (n):
  name.add(input())
for _ in range (m):
  nosee = input()
  if nosee in name:
    answer.append(nosee)
answer.sort()
print(len(answer))
for a in answer:
  print(a)