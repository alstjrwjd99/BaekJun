document= input()
search = input()
pointer = 0
answer = 0
l_search = len(search)
l_document = len(document)
while pointer < l_document - l_search + 1:
  for i in range (l_search):
    if search[i] != document[i+pointer]:
      pointer += 1
      break
    if i+1 == l_search :
      answer += 1
      pointer += l_search
    
print(answer)