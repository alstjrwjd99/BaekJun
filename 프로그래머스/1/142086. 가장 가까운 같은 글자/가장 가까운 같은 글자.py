def solution(s):
    answer = []
    str_idx = dict()
    for idx,alpha in enumerate(s) :
        if alpha in str_idx :
            answer.append(idx - str_idx[alpha])
        else :
            answer.append(-1)
        str_idx[alpha] = idx
    return answer