for test_case in range(1, 11):
    a = int(input())
    buildings = list(map(int, input().split()))
    ans = 0

    for i in range(2, a - 2):
        if max(buildings[i-2 : i + 3]) == buildings[i]:
            high = max(max(buildings[i-2:i]), max(buildings[i+1 : i +3]))
            ans += buildings[i] - high

    print(f'#{test_case} {ans}')