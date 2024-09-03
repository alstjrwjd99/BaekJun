import sys
input = sys.stdin.readline

n = int(input())

dance = set(['ChongChong'])
for i in range (n):
    a,b = input().split()
    if a in dance or b in dance:
        dance.add(a)
        dance.add(b)
print(len(dance))