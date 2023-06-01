N = int(input())
cookie = []
for _ in range (N):
  cookie.append(input())

heart = [0,0]
body = [0,0,-2,-1,-1]
def head(i,j):
  if cookie[i][j] =='*' and cookie[i][j-1]=='_':
    heart[0] = i+1
    heart[1] = j

for i in range(N):
  for j in range(N):
    if not heart[0]:
      head(i,j)
    #왼팔
    if i == heart[0] and cookie[i][j] =="*" and j < heart[1]:
      body[0] += 1
    #오른팔
    if i == heart[0] and cookie[i][j] =="*" and j > heart[1]:
      body[1] += 1
    #허리
    if j == heart[1] and cookie[i][j] =="*":
      body[2] += 1
    #왼쪽다리
    if j == heart[1]-1 and cookie[i][j] =="*":
      body[3] += 1
    #오른쪽다리
    if j == heart[1]+1 and cookie[i][j] =="*":
      body[4] += 1
for i in heart:
  print(i+1,end = ' ')
print()
for j in body:
  print(j, end  = ' ')