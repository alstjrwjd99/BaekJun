import sys
N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
A = [0]*1003 
for i in num:  
    A[i] += 1

result = []
i = 0
while sum(A) > 0:
    flag = 1
    if A[i] and A[i+1]:
        for x in range(i+2,1001):
            if A[x]:
                result += [i] * A[i]
                A[i] = 0
                result.append(x)
                A[x] -= 1
                flag = 0
                break

        if flag :
            result += [i+1]*A[i+1]
            A[i+1] = 0
            result += [i]*A[i]
            A[i] = 0 

    else :
        result += [i] * A[i]
        A[i] = 0
    i += 1
print(*result)