def solution(n, results):
    answer = 0
    vtx =[[''] * (n+1) for _ in range (n+1)]
    for win, lose in results:
        vtx[win][lose] = 'win'
        vtx[lose][win] = 'lose'
    
    for k in range (n+1):
        for i in range (n+1):
            for j in range (n+1):
                if vtx[i][k] == vtx[k][j] != '':
                    vtx[i][j] = vtx[i][k]
    
    for i in range (1,n+1):
        can_rank = True
        for j in range (1,n+1):
            if i == j : continue
            if vtx[i][j] == '': can_rank = False
        if can_rank : answer += 1
    return answer