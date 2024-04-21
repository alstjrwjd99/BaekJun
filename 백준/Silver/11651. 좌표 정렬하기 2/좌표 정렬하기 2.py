import sys
input = sys.stdin.readline
n = int(input())
num = []
for _ in range (n):
    num.append(tuple(map(int,input().split())))
num.sort(key=lambda x : (x[1],x[0]))
for i in num:
    print(*i)