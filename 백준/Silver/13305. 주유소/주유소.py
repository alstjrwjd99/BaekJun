import sys
input = sys.stdin.readline

n = int(input())
dist = list(map(int,input().split()))
oil_cost = list(map(int,input().split()))

# 자기보다 작아질때까지만 가면됨
answer = 0
minium_cost = 1e9
for i in range (n-1):
    if minium_cost >= oil_cost[i]:
        minium_cost = oil_cost[i]
        answer += oil_cost[i] * dist[i]
    else :
        answer += minium_cost * dist[i]
print(answer)