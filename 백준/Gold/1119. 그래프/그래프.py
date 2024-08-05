def dfs(graph, visited, node):
    stack = [node]
    size = 0
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            size += 1
            for neighbor in graph[v]:
                if not visited[neighbor]:
                    stack.append(neighbor)
    return size

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    if N == 1:
        print(0)
        return

    graph = [[] for _ in range(N)]
    cnt = 0

    index = 1
    for i in range(N):
        a = data[index]
        index += 1
        for j in range(len(a)):
            if a[j] == 'Y':
                graph[i].append(j)
                cnt += 1

    cnt //= 2

    visited = [False] * N
    sizes = []

    for i in range(N):
        if not visited[i]:
            sizes.append(dfs(graph, visited, i))

    sum_edges = sum(size - 1 for size in sizes)

    for size in sizes:
        if size == 1:
            print(-1)
            return

    if len(sizes) - 1 <= cnt - sum_edges:
        print(len(sizes) - 1)
    else:
        print(-1)

if __name__ == "__main__":
    main()