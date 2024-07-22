import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
team = list(map(int, input().split()))
dp = [0] * N
result = [0] * N

for i in range(N):
    p = team[i]
    if i == 0:
        dp[i] = p
    else:
        dp[i] = dp[i - 1] + p
        result[i] = result[i - 1] + p * dp[i - 1]
dp = [0] + dp
result = [0] + result

for _ in range(Q):
    s, e = map(int, input().split())
    ans = result[e]
    if s == 1:
        print(ans)
    else:
        temp = (dp[e] - dp[s - 1]) * dp[s - 1]
        print(ans - temp - result[s - 1])

