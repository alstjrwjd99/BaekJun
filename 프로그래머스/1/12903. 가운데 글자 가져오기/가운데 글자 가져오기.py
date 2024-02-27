def solution(s):
    len_s = len(s)
    if len_s % 2 == 0 :
        answer = s[len_s//2-1:len_s//2+1]
    else :
        answer = s[len_s//2]
    return answer