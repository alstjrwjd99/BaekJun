import string
def solution(s, n):
    answer = ''
    low = list(string.ascii_lowercase)
    up = list(string.ascii_uppercase)
    
    for i in s :
        if i in low:
            answer += low[(low.index(i)+n)%26]
        elif i in up :
            answer += up[(up.index(i)+n)%26]
        else :
            answer += ' '
    return answer