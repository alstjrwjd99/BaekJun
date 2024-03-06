def solution(a, b, n):
    answer = 0
    have = n
    while True :
        give = have // a 
        have = (have % a) + (give * b)
        answer += (give * b)
        if give == 0 :
            break
    return answer