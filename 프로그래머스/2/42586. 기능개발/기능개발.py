import math

def solution(progresses, speeds):
    answer = []
    remain = []
    for progress, speed in zip(progresses, speeds):
        remain.append(math.ceil((100-progress) / speed))
        
    max_day = remain[0]
    cnt = 0
    for done in remain:
        if max_day >= done:
            cnt += 1
        else : 
            answer.append(cnt)
            max_day = done
            cnt = 1
    answer.append(cnt)
    return answer