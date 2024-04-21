import sys
input = sys.stdin.readline
n = int(input())
have = set(map(int, input().split()))
m = int(input())
compare = list(map(int, input().split()))

for i in compare:
    if i in have:
        print(1,end=' ')
    else :
        print(0,end=' ')