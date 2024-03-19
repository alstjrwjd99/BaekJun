N,M = map(int,input().split(' '))
a=set([input() for i in range(N)])
b=set([input() for i in range(M)])

c=list(a & b)

print(len(c))
c.sort()
for i in c:
    print(i) 