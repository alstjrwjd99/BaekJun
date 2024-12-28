import sys
input = sys.stdin.readline

from collections import Counter

n,m = map(int,input().split())
words = []
for _ in range (n):
    word = input().strip()
    if len(word) >= m : words.append(word)

c = Counter(words)
for a in sorted(list(c.items()), key=lambda x : (-x[1], -len(x[0]), x[0])):
    print(a[0])