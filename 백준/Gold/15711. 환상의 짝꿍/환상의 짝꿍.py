n=2*(10**6)
a=[False,False]+[True]*(n-1)
for i in range(2,int(n**0.5)+1):
    if a[i]:
        for j in range(2*i,n+1,i):
            a[j]=False
prime=[i for i in range(2,n) if a[i]]
for _ in range(int(input())):
    a,b=map(int,input().split())
    if a+b<4:
        print("NO")
    elif not (a+b)%2:
        print("YES")
    else:
        if a+b-2>=n:
            flag=0
            for p in prime:
                if not (a+b-2)%p:
                    flag=1
                    print("NO")
                    break
            if not flag:
                print("YES")
        else:
            if a+b-2 in prime:
                print("YES")
            else:
                print("NO")