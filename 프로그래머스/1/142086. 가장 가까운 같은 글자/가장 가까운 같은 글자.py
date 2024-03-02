def solution(s):
    answer = [0] * len(s)
    sets = {i : 0 for i in set(s)}
    for index,alpha in enumerate (s):
        if sets[alpha] == 0:
            answer[index] = -1
        else :
            answer[index] = index+1 - sets[alpha]
        sets[alpha] = index+1
    return answer