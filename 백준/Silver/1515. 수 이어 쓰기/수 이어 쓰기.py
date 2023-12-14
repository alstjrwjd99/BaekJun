isin = input()
i = 0
while True:
  i+=1
  stringNum = str(i)
  while len(stringNum) > 0 and len(isin) >0 :
    if stringNum[0] == isin[0]:
      isin = isin[1:]
    stringNum = stringNum[1:]
  if isin == '':
    print(i)
    break