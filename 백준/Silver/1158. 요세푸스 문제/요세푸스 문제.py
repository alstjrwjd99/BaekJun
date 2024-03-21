n, k = map(int,input().split())
yose = [i+1 for i in range (n)]
del_point = k-1
answer = []
while yose:
  answer.append(yose[del_point])
  yose.remove(yose[del_point])
  if len(yose) == 0:
    break
  del_point = (del_point + k-1) % len(yose)
print('<' + ', '.join(map(str, answer)) + '>')