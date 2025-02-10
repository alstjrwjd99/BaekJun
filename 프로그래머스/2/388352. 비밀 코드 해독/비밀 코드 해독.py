from itertools import combinations

def solution(n, q, ans):
    answer = 0
    for combi in list(combinations(range(1,n+1),5)):
        flag = True
        for i in range (len(q)) :
            if len(set(combi) & set(q[i])) != ans[i]:
                flag = False
                break
        if flag :
            answer += 1
    return answer