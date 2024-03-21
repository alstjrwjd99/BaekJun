def solution(genres, plays):
    answer = []
    streaming = dict()
    each_played = dict()
    for idx,(i,j) in enumerate(zip(genres,plays)):
        if i not in streaming:
            each_played[i] = [(idx,j)]
            streaming[i] = j
        else :
            each_played[i].append((idx,j))
            streaming[i] += j

    chart = []
    for playtime in streaming:
        chart.append((streaming[playtime],playtime))
    chart.sort(reverse = True)
    for gen in chart:
        if len(each_played[gen[1]]) == 1:
            answer.append(each_played[gen[1]][0][0])
        else:
            each_played[gen[1]].sort(key = lambda x : (-x[1],x[0]))
            answer.append(each_played[gen[1]][0][0])
            answer.append(each_played[gen[1]][1][0])
    return answer