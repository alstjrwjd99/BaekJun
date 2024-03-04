import string
#대문자 불러오는 패키지
alpha = string.ascii_uppercase
word = input()
answer = ''
for s in word:
  answer += alpha[(alpha.index(s)+23)%26]
print(answer)