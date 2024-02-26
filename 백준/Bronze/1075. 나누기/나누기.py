n = int(input())
f = int(input())
over = (n // 100) * 100
for i in range (0, 100):
  if (over + i) % f == 0 :
    print("{:02d}".format(i))
    break