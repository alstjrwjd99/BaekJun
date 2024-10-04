import sys
import math
input = sys.stdin.readline

first, end = map(int, input().split())
isSqrtNoNo = [True] * (end - first + 1)

first_sqrt = int(math.sqrt(first))
end_sqrt = int(math.sqrt(end)) + 1

# 제곱수를 기준으로 해당 범위 내에서 나누어떨어지는 값을 처리합니다.
for i in range(2, end_sqrt):
    square = i * i
    # 시작 지점을 설정합니다.
    start = max(square, (first + square - 1) // square * square)

    for j in range(start, end + 1, square):
        isSqrtNoNo[j - first] = False

# 제곱수가 아닌 수의 개수를 세기
print(sum(isSqrtNoNo))