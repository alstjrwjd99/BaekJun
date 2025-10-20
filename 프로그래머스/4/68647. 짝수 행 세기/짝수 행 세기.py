import sys
sys.setrecursionlimit(10000000)

MOD = 10**7 + 19
comb_list = [[0]*301 for _ in range(301)]

def combination(n, r):
    if n == 1 or n == r or r == 0:
        return 1
    if comb_list[n][r]:
        return comb_list[n][r]
    comb_list[n][r] = (combination(n-1, r-1) + combination(n-1, r)) % MOD
    return comb_list[n][r]

def count_1s(a, col, row):
    res = []
    for i in range(row):
        cnt = 0
        for j in range(col):
            cnt += a[j][i]
        res.append(cnt)
    return res

def make_dp(col, row, lst):
    dp = [[0]*(col+1) for _ in range(row)]
    dp[0][col - lst[0]] = combination(col, lst[0])

    for i in range(row-1):
        for j in range(col+1):
            if dp[i][j]:
                tot_num = lst[i+1]
                for k in range(min(tot_num, j)+1):
                    if col - j < tot_num - k:
                        continue
                    even = j + tot_num - 2*k
                    dp[i+1][even] += (
                        dp[i][j] *
                        combination(j, k) *
                        combination(col - j, tot_num - k)
                    ) % MOD
                    dp[i+1][even] %= MOD
    return dp

def solution(a):
    col, row = len(a), len(a[0])
    one_list = count_1s(a, col, row)
    dp = make_dp(col, row, one_list)
    return dp[-1][-1] % MOD