def solution(brown, yellow):
    a=1
    while True:
        b=(brown+4-2*a)/2
        if (a-2)*(b-2)==yellow:
            break
        a+=1
    b=int(b)
    answer=[max(a,b),min(a,b)]
    return answer