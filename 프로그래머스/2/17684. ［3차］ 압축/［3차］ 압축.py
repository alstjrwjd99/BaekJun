# 입력된 글자의 최대 존재하는 만큼을 인덱스 return, 한글자 더 있으면 그 글자를 사전에 추가
def solution(msg):
    answer = []
    lzw = {chr(i+65) : i+1 for i in range (26)}
    idx = 27
    check = 0
    test = ''
    for i in range (len(msg)):
        if i < check :
            continue
        j = 1
        while i+j <= len(msg):
            j += 1
            if msg[i:i+j] not in lzw:
                answer.append(lzw[msg[i:i+j-1]])
                check += j-1
                break
        if msg[i:i+j] not in lzw: 
            lzw[msg[i:i+j]] = idx
            idx += 1
        
    if msg[check:] in lzw:
        answer.append(lzw[msg[check:]])
    return answer