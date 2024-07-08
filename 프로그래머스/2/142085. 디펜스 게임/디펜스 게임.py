from heapq import heappush, heappop

def solution(n, k, enemy):
    h = []
    for i, e in enumerate(enemy):
        heappush(h, e)
        if len(h) > k:
            n -= heappop(h)
        if n < 0:
            return i

    return len(enemy)