import sys
input = sys.stdin.readline

N = int(input())
coor = list(map(int, input().split()))

set_coor = set(coor)
sort_coor = sorted(list(set_coor))
comp = dict()

for i in range (len(sort_coor)):
    comp[sort_coor[i]] = i

for c in coor:
    print(comp[c], end=' ')
