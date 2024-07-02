def solution(tickets):
    n = len(tickets)
    answer = []
    def dfs():
        if len(stack) == n+1 :
            a = [stack[i] for i in range(n+1)]
            answer.append(a)
        for i in range(n):
            if not visited[i] and stack[-1] == tickets[i][0] :
                visited[i] = 1
                stack.append(tickets[i][1])
                dfs()
                visited[i] = 0
                stack.pop()

    for i in range(n):
        visited = [0] * n
        stack = []
        if tickets[i][0] == "ICN":
            visited[i] = 1
            stack.append(tickets[i][0])
            stack.append(tickets[i][1])
            dfs()

    return min(answer)