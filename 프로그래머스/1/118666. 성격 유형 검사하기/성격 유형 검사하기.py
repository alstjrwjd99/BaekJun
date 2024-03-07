def solution(survey, choices):
    answer = ''
    #R T
    #C F
    #J M
    #A N
    mbti = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    for idx,pro in enumerate (survey):
        if choices[idx] < 4 :
            mbti[pro[0]] += 4 - choices[idx]
        elif choices[idx] > 4 :
            mbti[pro[1]] += choices[idx] - 4
    answer += 'R' if mbti['R'] >= mbti['T'] else 'T'
    answer += 'C' if mbti['C'] >= mbti['F'] else 'F'
    answer += 'J' if mbti['J'] >= mbti['M'] else 'M'
    answer += 'A' if mbti['A'] >= mbti['N'] else 'N'    
    return answer