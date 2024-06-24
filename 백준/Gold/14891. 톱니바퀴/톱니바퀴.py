import sys
input = sys.stdin.readline

tobnis = [
    list(map(int, list(input().strip())))
    for _ in range(4)    
]

K = int(input())
ways = [
    list(map(int, input().split()))
    for _ in range(K)    
]

def rotate(tobni, way):
    if way == 1:  # 시계 방향
        return [tobni[-1]] + tobni[:-1]
    else:  # 반시계 방향
        return tobni[1:] + [tobni[0]]

for way in ways:
    n, direction = way[0] - 1, way[1]
    directions = [0] * 4
    directions[n] = direction

    # 오른쪽으로 전파
    for i in range(n, 3):
        if tobnis[i][2] != tobnis[i + 1][6]:
            directions[i + 1] = -directions[i]
        else:
            break

    # 왼쪽으로 전파
    for i in range(n, 0, -1):
        if tobnis[i][6] != tobnis[i - 1][2]:
            directions[i - 1] = -directions[i]
        else:
            break

    # 각 톱니바퀴 회전 적용
    for i in range(4):
        if directions[i] != 0:
            tobnis[i] = rotate(tobnis[i], directions[i])

ans = 0
for i in range(4):
    if tobnis[i][0] == 1:
        ans += 2 ** i

print(ans)