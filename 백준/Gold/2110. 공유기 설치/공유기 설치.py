import sys
input = sys.stdin.readline

N,C = map(int,input().split())

house = [int(input()) for _ in range(N)]
house.sort()

left = 1
right = house[-1]

answer = 0

while left <= right:
    mid = (left + right) // 2
    current = house[0]
    count = 1

    for i in range(1,N):
        if house[i] >= current + mid:
            count += 1
            current = house[i]
            
    if count >= C:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)   