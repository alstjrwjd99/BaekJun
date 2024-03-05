s = input()
answer = []
for i in range (len(s)) :
  answer.append(s[i:])
answer.sort()
for a in answer:
  print(a)