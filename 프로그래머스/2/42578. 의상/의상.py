def solution(clothes):
    answer = 1
    box = dict()
    for cset in clothes:
        if cset[1] not in box :
            box[cset[1]] = 1
        else :
            box[cset[1]] += 1
    for kind in box.values():
        answer *= kind+1
    return answer - 1