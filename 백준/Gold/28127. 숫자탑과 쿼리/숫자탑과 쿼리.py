import sys
input = sys.stdin.readline

Q = int(input())

# 등차 합공식
def get_left(a, d, n):
    return (n - 1) * (2 * a + (n - 2) * d) // 2 + 1

for _ in range(Q):
    a, d, value = map(int, input().split())
    start, end = 1, 1000000
    x, y = 0, 0

    while start <= end:
        middle = (start + end) // 2
        left = get_left(a, d, middle)

        if left <= value:
            start = middle + 1
            x = left
            y = middle
        else:
            end = middle - 1

    print(y, value - x + 1)