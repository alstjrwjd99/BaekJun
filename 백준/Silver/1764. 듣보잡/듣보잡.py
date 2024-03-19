N,M = map(int,input().split(' ')) 
a =set([input() for i in range(N)]) #듣지못한사람 set생성
b=set([input() for i in range(M)]) # 보지못한사람 set생성

c=sorted(list(a & b)) #듣보잡 (set의 교집합 사용)

print(len(c))
for i in c:
    print(i)
