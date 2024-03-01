def solution(today, terms, privacies):
    answer = []
    today = today.split('.')
    today = int(today[0]+today[1]+today[2])
    ter = {}
    for term in terms:
        tmp = term.split()
        ter[tmp[0]] = tmp[1]
    for key, pri in enumerate(privacies):
        tmp = pri.split()
        day = list(map(int,tmp[0].split('.')))
        month = day[1] + int(ter[tmp[1]]) 
        # 월
        if month > 12 :
            if month % 12 == 0:
                day[0] += month // 12 - 1            
                day[1] = 12
            else :
                day[0] += month // 12
                day[1] = month % 12
        else :
            day[1] = month
        # 일
        if day[2] - 1 == 0 :
            if day[1] - 1 == 0 :
                day[0] -= 1
                day[1] = 12
                day[2] = 28
            else :
                day[1] -= 1
                day[2] = 28
        else :
            day[2] -= 1
        dueDay = int(str(day[0]) + str(day[1]).zfill(2) + str(day[2]).zfill(2))
        if today > dueDay:
            answer.append(key+1)

    return answer
