def solution(dartResult):
    answer = 0  
    score = []
    for i in range (len(dartResult)):
        #숫자 추출
        if dartResult[i].isdigit():
            if dartResult[i] == '1' and dartResult[i+1] == '0':
                score.append(10)
            elif dartResult[i] == '0' and dartResult[i-1] == '1':
                continue
            else :
                score.append(int(dartResult[i]))
        #보너스 계산
        else :
            if dartResult[i] == 'D':
                score[-1] = score[-1] ** 2
            elif dartResult[i] == 'T':
                score[-1] = score[-1] ** 3
        #옵션 계산
            if dartResult[i] == '*':
                if len(score) > 1:
                    score[-2] *= 2
                    score[-1] *= 2
                else :
                    score[-1] *= 2
            elif dartResult[i] == '#':
                score[-1] *= (-1)
    return sum(score)