T = int(input())
for _ in range(T):
    N = int(input())
    stock = list(map(int, input().split()))
    stock.reverse()
    max = stock[0]
    sum = 0

    for i in range(1, N):
        if max < stock[i]:
            max = stock[i]
            continue
        sum += max - stock[i]

    print(sum)    