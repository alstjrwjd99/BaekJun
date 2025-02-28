from collections import deque

n, k = map(int, input().split())
visit = [[-1, -1] for _ in range(500001)]

def move(idx, now):
    if idx == 0:
        return now + 1
    if idx == 1:
        return now - 1
    return 2 * now

def bfs(now, k):
    q = deque()
    second = 0
    q.append((now, second))
    visit[now][0] = 0
    while q:
        for _ in range(len(q)):
            now, second = q.popleft()
            for idx in range(3):
                next = move(idx, now)
                if not(0 <= next < 500001): continue
                if visit[next][(second + 1) % 2] != -1: continue
                q.append((next, second + 1))
                visit[next][(second + 1) % 2] = second + 1

bfs(n, k)
ans = -1
second = 0

for i in range(500001):
    k += i
    if k > 500000: break
    if visit[k][second % 2] <= second:
        ans = second
        break
    second += 1
print(ans)