N,M = map(int,input().split())
card = list(map(int,input().split()))
answer = 0
for i in range (N) :
  for j in range (i+1,N) :
    for k in range (j+1,N):
      cardSum = card[i] + card[j] +card[k]
      if cardSum < M and answer <= cardSum :
        answer = cardSum        
      elif cardSum == M :
        answer = cardSum
        break        
print(answer)