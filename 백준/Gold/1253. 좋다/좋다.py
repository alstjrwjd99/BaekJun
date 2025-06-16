import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

a.sort()

answer = 0

for i in range(n):
    goal = a[i]
    start = 0
    end = n - 1
    while start < end:
        if a[start] + a[end] == goal:
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else :
                answer += 1
                break
        elif a[start] + a[end] < goal:
            start += 1
        else:
            end -= 1
print(answer)