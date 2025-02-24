import sys

input = sys.stdin.readline

k = int(input())

for _ in range(k):
    n, m = map(int, input().split())

    arr = []

    for _ in range(m):
        arr.append(list(map(int, input().split())))

    book = [i for i in range(1,n+1)]

    arr.sort(key=lambda x:x[1]) # b를 기준으로 정렬
    cnt = 0

    for a, b in arr:
        for i in range(a, b + 1):
            if i in book:
                cnt += 1
                book.remove(i)
                break

    print(cnt)