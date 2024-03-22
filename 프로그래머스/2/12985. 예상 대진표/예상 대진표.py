def solution(n,a,b):
    r = 1
    a,b = min(a,b),max(a,b)
    while not (a%2==1 and b%2==0 and a+1==b):
        r += 1
        a = a//2 + a%2
        b = b//2 + b%2
    return r