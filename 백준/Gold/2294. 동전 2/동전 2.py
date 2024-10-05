'''
coins에 있는 숫자들을 최소로 사용해서 합이 K가 되는 개수
dp 에다가 만들 수 있는 최소 개수 갱신
'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = list(set([int(input()) for _ in range(N)]))
dp = [1e9] * (K + 1)
dp[0] = 0  # 합이 0이 되는 경우는 동전을 하나도 사용하지 않으므로 0개

# 각 동전의 값을 사용해서 dp 테이블을 갱신
for coin in coins:
    for i in range(coin, K + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

# 결과 출력
if dp[K] == 1e9:
    print(-1)  # K를 만들 수 없는 경우
else:
    print(dp[K])