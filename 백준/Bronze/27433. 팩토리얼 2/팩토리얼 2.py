import sys
input = sys.stdin.readline
n = int(input())

def sol(n, acc):
    if n == 0:
        return acc
    return sol(n-1, acc * n)
   
print(sol(n, 1))