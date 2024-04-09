def solution():
    check = 0
    if len(answer) == m:
        print(*answer)
        return
    for i in range(n):
        if check != num[i] and visited[i] == 0:
            answer.append(num[i])
            visited[i] = 1
            check = num[i]
            solution()
            answer.pop()
            visited[i] = 0


n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))
visited = [0] * n
answer = []
solution()