path = input()
stack = []
answer = 0

# () -> 레이져, (()()) -> 막대( 레이져 ()  레이져 ()  )막대
for i in range (len(path)):
  if path[i] == '(':
    stack.append(path[i])
  else :
    # 현재 쇠막대기 카운팅
    if path[i-1] == '(':
      stack.pop()
      answer += len(stack)
    # 레이저 카운트
    else :
      stack.pop()
      answer += 1
print(answer)