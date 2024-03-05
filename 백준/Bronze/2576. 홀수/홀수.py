all = 0
mini = 102
for i in range (7):
 num = int(input())
 if num % 2 == 1:
  all += num
  mini = num if mini > num else mini
print(-1) if all == 0 else print(all)
if all !=0 : print(mini)