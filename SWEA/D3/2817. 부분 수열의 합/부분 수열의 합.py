T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    # 합이 0이 되는 경우는 요소를 선택하지 않는 한 가지 방법뿐이므로 dp[0][0]을 1로 설정
    dp[0][0] = 1

    # 각 숫자를 순회
    for i in range(1, N + 1):
        # 0부터 K까지의 가능한 합을 순회
        for j in range(K + 1):
            # 경우 1: 현재 숫자를 포함하지 않는 경우 (이전 숫자까지의 경우의 수 그대로)
            dp[i][j] += dp[i - 1][j]
            # 경우 2: 현재 숫자를 포함하는 경우 (현재 숫자를 포함해도 합이 j를 넘지 않는 경우)
            before = j - numbers[i - 1]
            if before >= 0:
                dp[i][j] += dp[i - 1][before]

    result = dp[N][K]
    print(f"#{test_case} {result}")
