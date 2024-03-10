def solution(picks, minerals):
    answer = 0
    mine = [[0,0,0] for _ in range (len(minerals)//5+1)]
    limit = sum(picks) * 5
    if len(minerals) > limit:
        minerals = minerals[:limit]
    for i in range (len(minerals)) :
        if minerals[i] == 'diamond':
            mine[i//5][0] += 1
        elif minerals[i] == 'iron':
            mine[i//5][1] += 1
        elif minerals[i] == 'stone':
            mine[i//5][2] += 1
    mine.sort(key = lambda x : (-x[0],-x[1],-x[2]))
    print(mine)
    for i in mine:
        dia,iron,stone = i
        for j in range(len(picks)):
            if picks[j]>0 and j==0:
                picks[j]-=1
                answer += dia + iron + stone
                break
            elif picks[j]>0 and j==1:
                picks[j]-=1
                answer += (5*dia) + iron + stone
                break
            elif picks[j]>0 and j==2:
                picks[j]-=1
                answer += (25*dia) + (5*iron) + stone
                break
    return answer