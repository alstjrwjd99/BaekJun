import string
alpha = string.ascii_lowercase
s = input()
for i in alpha:
  if i in s :
    print(s.index(i), end =' ')
  else :
    print(-1, end = ' ')