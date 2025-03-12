import sys
input = sys.stdin.readline
import heapq

n = int(input())
oil_tank = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[0])
destination, p = map(int, input().split())

hq = []
can_go = p
answer = 0
cannot_go = False

for dist, oil in oil_tank:
    while dist > can_go:
        if hq:
            can_go -= heapq.heappop(hq)
            answer += 1
        else:
            cannot_go = True
            break
    if cannot_go:
        break
    heapq.heappush(hq, -oil)

if not cannot_go:
    while destination > can_go:
        if hq:
            can_go -= heapq.heappop(hq)
            answer += 1
        else:
            answer = -1
            break
else:
    answer = -1

print(answer)