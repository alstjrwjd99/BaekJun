N = int(input())
answer =1 
around = 1
i = 1
while around < N:
    around += 6 * i
    i += 1
    answer += 1
print(answer)