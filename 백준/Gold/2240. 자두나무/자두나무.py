import sys
input = sys.stdin.readline

T, W = map(int, input().split())
jadu = [0] + [int(input().strip()) for _ in range(T)] 

dp = [[0] * (W + 1) for _ in range(T + 1)]

if jadu[1] == 1:
    dp[1][0] = 1
    dp[1][1] = 0
else:
    dp[1][0] = 0
    dp[1][1] = 1

for t in range(2, T + 1):
    for w in range(W + 1):
        # 현재 떨어지는 자두가 1번 나무인지 2번 나무인지 판단
        if (w % 2 == 0 and jadu[t] == 1) or (w % 2 == 1 and jadu[t] == 2):
            dp[t][w] = max(dp[t-1][w], dp[t-1][w-1] if w > 0 else 0) + 1
        else:
            dp[t][w] = max(dp[t-1][w], dp[t-1][w-1] if w > 0 else 0)

print(max(dp[T]))