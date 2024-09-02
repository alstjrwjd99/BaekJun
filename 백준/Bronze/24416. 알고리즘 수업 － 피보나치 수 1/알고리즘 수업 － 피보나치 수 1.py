import sys
input = sys.stdin.readline

n = int(input())

global c1,c2
c1,c2 = 0,1
def fib(n) :
    global c1
    c1 += 1
    if (n == 1 or n == 2) :
      return 1
    return (fib(n - 1) + fib(n - 2))

f = [0,1,1]
def fibonacci(n) :
    global c2
    for i in range  (3 , n):
        c2 += 1
        f.append(f[i - 1] + f[i - 2])
    return f[n-1]

fib(n)
print((c1+1)//2,end = ' ')
fibonacci(n)
print(c2)