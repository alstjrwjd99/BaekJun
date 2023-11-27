N = int(input())
answer = 0
room = []
endTime = 0
for _ in range (N):
  room.append(list(map(int,input().split())))

room.sort(key = lambda x : (x[1],x[0]))
for i in room:
  if endTime <= i[0]:
    endTime = i[1]

    answer += 1
print(answer)