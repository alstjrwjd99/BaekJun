def solution(s):
    result = []
    s = s.split(' ')
    for sentence in s:
        answer = ''
        for idx,sen in enumerate (sentence):
            if idx % 2 == 0:
                answer += sen.upper()
            else :
                answer += sen.lower()
        result.append(answer)
    return ' '.join(result) 