n = int(input())
answer = 1
for i in range (1,n+1):
    answer *= i
if n == 0:
    print(1)
else : print(answer)