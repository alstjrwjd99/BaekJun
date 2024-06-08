def solution(s):
    answer = []
    tmp = s[1:-2].split('},')
    tup = []
    for i in tmp:
        tup.append(set(i[1:].split(',')))
    tup.sort(key =lambda x : len(x))
    
    answer.append(int(list(tup[0])[0]))
    for i in range (len(tup)-1):
        answer.append(int(list(tup[i+1] - tup[i])[0]))
        
    return answer