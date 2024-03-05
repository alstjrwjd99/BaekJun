N,M = map(int,input().split())
arra = list(map(int,input().split()))
arrb = list(map(int,input().split()))
poa, pob = 0,0
answer = []
while True:
  if poa == N :
    answer.extend(arrb[pob:])  
    break
  if pob == M :
    answer.extend(arra[poa:])  
    break  
  if arra[poa] <= arrb[pob] :
    answer.append(arra[poa])
    poa += 1
  else : 
    answer.append(arrb[pob])
    pob += 1
print(*answer)