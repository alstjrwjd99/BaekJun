'''
1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
2. X가 2로 나누어 떨어지면, 2로 나눈다.
3. 1을 뺀다.

3개 연산을 이용해서 1을 만들기
'''
n = int(input())

def sol(n):
    dp = [0] * (n+1)
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 1
    dp[2] = 1
    dp[3] = 1
    for i in range (4,n+1):
        a,b = 10000000,10000000
        if i % 3 == 0:
            a = dp[i//3] + 1
        if i % 2 == 0:
            b = dp[i//2] + 1
        c = dp[i-1] + 1
        dp[i] = min(a,b,c)
    return dp[n]
print(sol(n))