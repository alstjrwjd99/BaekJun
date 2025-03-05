import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
sensor = sorted(list(map(int,input().split())))

diff = []
for i in range (n -1):
    diff.append(abs(sensor[i+1] - sensor[i]))

diff.sort()

print(sum(diff[:n-k]))