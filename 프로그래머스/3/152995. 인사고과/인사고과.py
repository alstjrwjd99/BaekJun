def solution(scores):
    answer = 0
    wanho = scores[0]
    scores.sort(key=lambda x : (-x[0],x[1]))
    cutline = scores[0][1]
    worst = set()
    for score in scores:
        if score[1] < cutline :
            if score == wanho:
                return -1
            worst.add(tuple(score))
        cutline = max(cutline,score[1])    
    
    incentive_list = []
    for score in scores : 
        if tuple(score) not in worst:
            incentive_list.append(score)        
    
    incentive_list.sort(key=lambda x:-sum(x))
    pure_rank = incentive_list.index(wanho)
    if pure_rank == 0:
        return 1
    
    while True:
        if sum(incentive_list[pure_rank]) == sum(incentive_list[pure_rank-1]):
            pure_rank -= 1
        else : break
    return pure_rank + 1