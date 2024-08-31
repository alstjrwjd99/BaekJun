def solution(money):
    answer = 0

    dp1 = [0] * len(money) # 첫 집을 털었을 때
    dp2 = [0] * len(money) # 첫 집을 안 털고 두 번째 집을 털었을 때
    # dp3 = [0] * len(money) # 첫 집과 두 번째 집을 안 털었을 때

    dp1[0] = money[0]
    dp1[1] = dp1[0]
    dp2[1] = money[1]

    for i in range(2, len(money) - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])
        # dp3[i] = max(dp3[i - 1], dp3[i - 2] + money[i])

    dp1[-1] = dp1[-2]
    dp2[-1] = max(dp2[-2], dp2[-3] + money[-1])
    # dp3[-1] = max(dp3[-2], dp3[-3] + money[-1])
    # answer = max(dp1[-1], dp2[-1], dp3[-1])
    answer = max(dp1[-1], dp2[-1])

    return answer