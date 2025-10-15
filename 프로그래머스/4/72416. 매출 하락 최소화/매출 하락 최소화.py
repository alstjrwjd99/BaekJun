from collections import defaultdict, deque

def solution(sales, links):
    n = len(sales)
    children = [[] for _ in range(n+1)]
    indeg = [0]*(n+1)
    for u, v in links:
        children[u].append(v)
        indeg[v] += 1

    root = next(i for i in range(1, n+1) if indeg[i] == 0)

    order = []
    stack = [root]
    while stack:
        u = stack.pop()
        order.append(u)
        for v in children[u]:
            stack.append(v)
    order.reverse()

    dp0 = [0]*(n+1)
    dp1 = [0]*(n+1)

    for u in order:
        dp1[u] = sales[u-1]
        sum0 = 0
        has_free = False
        extra = float('inf')

        for v in children[u]:
            dp1[u] += min(dp0[v], dp1[v])
            if dp0[v] < dp1[v]:
                sum0 += dp0[v]
                extra = min(extra, dp1[v] - dp0[v])
            else:
                sum0 += dp1[v]
                has_free = True

        dp0[u] = sum0
        if children[u] and not has_free:
            dp0[u] += extra

    return min(dp0[root], dp1[root])