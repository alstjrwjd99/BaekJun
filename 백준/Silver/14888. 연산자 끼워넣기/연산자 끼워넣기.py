from itertools import permutations

N = int(input())
num = list(map(int,input().split()))
operator = list(map(int,input().split()))
realOper = ['+','-','*','/']
op = ''
answer = []

def cal(n1,o,n2):
    if o == '+':
        return n1+n2
    if o == '-':
        return n1-n2
    if o == '*':
        return n1*n2
    if o == '/':
        if n1 < 0:
            return (abs(n1) // n2) * (-1)
        return n1//n2

# 연산자들을 기호로 바꿔서 표현
for idx,real in zip(operator,realOper):
    op += idx*real
op = list(op)
dummy = num[0]

# 모든 연산자의 경우의 수 만들기
allcom = list(permutations(op,len(op)))

for combo in allcom:
    # 숫자 & 기호로 계산하기
    for i in range (1,N):
        dummy = cal(dummy,combo[i-1],num[i])
    answer.append(dummy)
    dummy = num[0]
print(max(answer))
print(min(answer))