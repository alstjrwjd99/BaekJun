import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
relations = {i:set() for i in range (1,n+1)}
for _ in range(m):
    a,b = list(map(int,input().split()))
    relations[a].add(b)
    relations[b].add(a)

answer = set()

for rel in (relations[1]):
    answer.add(rel)
    for a in (relations[rel]):
        answer.add(a)
if 1 in answer:
    print(len(answer)-1)
else :
    print(0)