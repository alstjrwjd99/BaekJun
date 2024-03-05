n = int(input())
score = list(map(int,input().split()))
avg = sum(score)/n #분배법칙 
print(avg/max(score)*100)