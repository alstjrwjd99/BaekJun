import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0      
ans = -1     

def merge_sort(A, p, r):
    global cnt, ans, K
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    global cnt, ans, K
    i = p
    j = q + 1
    t = 0
    tmp = [0] * (r - p + 1)
    
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp[t] = A[i]
            t += 1
            i += 1
        else:
            tmp[t] = A[j]
            t += 1
            j += 1
    
    while i <= q:
        tmp[t] = A[i]
        t += 1
        i += 1
        
    while j <= r:
        tmp[t] = A[j]
        t += 1
        j += 1
    
    i = p
    t = 0
    while i <= r:
        A[i] = tmp[t]
        cnt += 1           
        if cnt == K:     
            ans = A[i]
        i += 1
        t += 1

merge_sort(A, 0, N - 1)
print(ans)