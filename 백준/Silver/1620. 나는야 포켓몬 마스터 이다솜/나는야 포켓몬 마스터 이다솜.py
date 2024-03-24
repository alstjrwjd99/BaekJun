import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dogam = dict()

for i in range(1, n + 1):
    a = input().rstrip()
    dogam[i] = a
    dogam[a] = i

for i in range(m):
    quest = input().rstrip()
    if quest.isdigit():
        print(dogam[int(quest)])
    else:
        print(dogam[quest])