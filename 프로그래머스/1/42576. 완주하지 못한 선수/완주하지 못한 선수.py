def solution(participant, completion):
    answer = ''
    n=len(participant)
    dic1={i:0 for i in participant}
    dic2={i:0 for i in participant}

    for i in participant:
        dic1[i]+=1
    for i in completion:
        dic2[i]+=1

    for i in dic1:
        if dic1[i]-dic2[i]==1:
            return i