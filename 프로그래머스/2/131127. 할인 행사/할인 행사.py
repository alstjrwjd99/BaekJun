def solution(want, number, discount):
    answer = 0
    # for문 돌리면서 [i:i+10] 안에 want가 number만큼 있는지 파악해 나가면서 있으면 answer += 1
    # in연산자를 쓰면 시간 초과가 날 것 같으니깐 처음 10개 비교하고 앞은 빼고 뒤는 넣고 계산
    setting = discount[0:10]
    contain = []
    for wana in want :
        contain.append(setting.count(wana))
    if contain == number:
        answer +=1
    for i in range (1,len(discount)-9):
        if discount[i-1] in want :
            contain[want.index(discount[i-1])] -= 1
        if discount[i+9] in want :
            contain[want.index(discount[i+9])] += 1
        if contain == number:
            answer +=1
    return answer