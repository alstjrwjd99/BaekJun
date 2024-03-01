def solution(s, skip, index):
    answer = ''
    alp = [chr(i + 97) for i in range (26)]
    for i in skip:
        alp.remove(i)
    for a in s:
        answer += (alp[(alp.index(a)+index)%len(alp)])
    return answer