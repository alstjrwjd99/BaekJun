def buy1(n): # 1개 살 경우
    global result
    result += 3 * x[n]

def buy2(n): # 2개 살 경우
    global result
    m = min(x[n:n+2])
    x[n] -= m
    x[n+1] -= m
    result += 5* m    

def buy3(n): # 3개 살 경우
    global result
    m = min(x[n:n+3])
    x[n] -= m
    x[n+1] -= m
    x[n+2] -= m
    result += 7* m
    
import sys
N = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split())) + [0,0]
result = 0
for i in range(len(x)-2):
    if x[i+1] > x[i+2]: # # 3번째가 더 작으면 -> [2, 3, 2, 1] 같은 케이스
        m = min(x[i], x[i+1] - x[i+2]) # x[i]랑 x[i+1]-x[i+2] 비교
        x[i] -= m
        x[i+1] -= m
        result += 5*m # 이 때는 3곳보단 2곳 사는게 이득
        buy3(i) # 남는 갯수는 3곳에서 사자
        buy1(i) # 마지막 남은건 그냥사자
    else :
        buy3(i)
        buy2(i)
        buy1(i)
print(result)