def solution(id_list, report, k):
    answer = []
    l_id = len(id_list)
    reported = [[0] * l_id for _ in range (l_id)]
    for re in report :
        tmp = re.split()
        give = tmp[0]
        take = tmp[1]
        reported[id_list.index(give)][id_list.index(take)] = 1 
    
    for i in range (l_id):
        over = 0
        for j in range (l_id):
            over += reported[j][i]
        if over < k:
            for a in range (l_id):
                reported[a][i] = 0
                
    for a in reported:
        answer.append(sum(a))
    
    
    return answer