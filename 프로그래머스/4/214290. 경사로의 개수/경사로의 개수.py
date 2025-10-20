MOD = 1_000_000_007

def solution(grid, d, k):
    n = len(grid)
    m = len(grid[0])
    N = n * m

    def idx(y, x): return y * m + x

    # 경사 s에 대한 전이행렬 A(s) (N×N)
    def build_adj_for_slope(s):
        A = [[0]*N for _ in range(N)]
        for y in range(n):
            for x in range(m):
                u = idx(y, x)
                h = grid[y][x]
                for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                    ny, nx = y+dy, x+dx
                    if 0 <= ny < n and 0 <= nx < m:
                        v = idx(ny, nx)
                        if grid[ny][nx] - h == s:
                            A[u][v] = 1
        return A

    def mat_mul(A, B):
        # 표준 O(N^3) 곱. N<=64라 충분함.
        N = len(A)
        C = [[0]*N for _ in range(N)]
        # 약간의 캐시 최적화
        for i in range(N):
            Ai = A[i]
            Ci = C[i]
            for k_ in range(N):
                aik = Ai[k_]
                if aik:
                    Bk = B[k_]
                    for j in range(N):
                        if Bk[j]:
                            Ci[j] = (Ci[j] + aik * Bk[j]) % MOD
        return C

    def mat_pow(M, e):
        # 빠른 거듭제곱
        N = len(M)
        R = [[0]*N for _ in range(N)]
        for i in range(N):
            R[i][i] = 1
        base = M
        while e > 0:
            if e & 1:
                R = mat_mul(R, base)
            base = mat_mul(base, base)
            e >>= 1
        return R

    # d 각 원소에 대해 전이행렬 만들고 한 바퀴 M 계산
    # M = A(d0) * A(d1) * ... * A(dL-1)
    L = len(d)
    # 첫 행렬
    M = build_adj_for_slope(d[0])
    for t in range(1, L):
        At = build_adj_for_slope(d[t])
        M = mat_mul(M, At)

    # k바퀴
    Mk = mat_pow(M, k)

    # 모든 시작/끝 허용 → Mk 모든 원소 합
    ans = 0
    for i in range(N):
        row = Mk[i]
        # 파이썬 sum은 빠름
        ans = (ans + sum(row)) % MOD
    return ans