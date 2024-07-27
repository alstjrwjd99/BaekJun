import sys
input = sys.stdin.readline

def solution(n, term):
    team_made = [False] * n
    visited = [False] * n

    def dfs(node):
        stack = []
        current = node

        while True:
            if visited[current]:
                if current in stack:
                    start = stack.index(current)
                    for i in range(start, len(stack)):
                        team_made[stack[i]] = True
                break

            visited[current] = True
            stack.append(current)
            current = term[current] - 1

    for i in range(n):
        if not visited[i]:
            dfs(i)
    
    return team_made.count(False)

T = int(input())
for _ in range(T):
    n = int(input())
    term = list(map(int, input().split()))
    print(solution(n, term))