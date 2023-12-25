import sys
import heapq

input = sys.stdin.readline

n = int(input())

cards = []
count = 0

for _ in range(n):
    heapq.heappush(cards, int(input()))

while len(cards) != 1:
    temp = heapq.heappop(cards) + heapq.heappop(cards)
    count += temp
    heapq.heappush(cards, temp)

print(count)