import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
books = defaultdict(int)

for _ in range (n):
    books[input().strip()] += 1

print(sorted(list(books.items()), key= lambda x :( -x[1], x[0])) [0][0])