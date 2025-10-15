'''
Union-find
시작은 아무곳에서나 함 -> 전체 방문 시 최소 비용이 얼마냐

문제에서 그림으로 힌트를 줬음
1. height 내에서 방문을 할 수 있는 애들을 그룹핑
2. 경계에 있는 애들 중 높이 차이가 최소인 곳에 사다리 설치 후 answer += 높이 차이
3. 그룹이 1개가 되면 종료
'''
def solution(land, height):
    n = len(land)
    parent = list(range(n*n))
    size = [1]*(n*n)

    def idx(i, j): return i*n + j

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb: 
            return False
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]
        return True

    edges = []
    for i in range(n):
        for j in range(n):
            if i+1 < n:
                diff = abs(land[i][j] - land[i+1][j])
                w = 0 if diff <= height else diff
                edges.append((w, idx(i,j), idx(i+1,j)))
            if j+1 < n:
                diff = abs(land[i][j] - land[i][j+1])
                w = 0 if diff <= height else diff
                edges.append((w, idx(i,j), idx(i,j+1)))
    edges.sort(key=lambda x: x[0])

    answer = 0
    used = 0
    for w, u, v in edges:
        if union(u, v):
            answer += w
            used += 1
            if used == n*n - 1:
                break

    return answer