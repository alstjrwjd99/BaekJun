T = int(input())
for _ in range (T):
  n = int(input())
  i = 0
  while n >= 1:
    if n % 2 == 1:
      print(i , end = ' ')
    n //= 2
    i += 1