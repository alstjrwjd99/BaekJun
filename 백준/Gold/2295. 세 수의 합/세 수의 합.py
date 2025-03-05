import sys
input=sys.stdin.readline

n = int(input())
u = set()
ans = -1

for i in range(n):
    u.add(int(input()))

sums=set()
for i in u:
    for j in u:
        sums.add(i+j)

for i in u:
    for j in u:
        if (i-j) in sums:
            ans = max(ans, i)
print(ans)
