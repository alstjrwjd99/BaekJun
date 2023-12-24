n, x = map(int,input().split())
bangmoon = list(map(int,input().split()))

if max(bangmoon) == 0 :
  print("SAD")
else : 
  ans2 = 1
  sumbangmoon = sum(bangmoon[0:x])
  answer = sumbangmoon
  for i in range (x,n):
    sumbangmoon -= bangmoon[i-x]
    sumbangmoon += bangmoon[i]
    if answer < sumbangmoon:
      answer = sumbangmoon
      ans2 = 1
    elif answer == sumbangmoon :
      ans2 += 1
  print(answer)
  print(ans2)