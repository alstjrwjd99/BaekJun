def solution(progresses, speeds):
    answer = []
    works = []
    for progress,speed in zip(progresses,speeds):
        remain = 100 - progress
        if remain % speed == 0:
            works.append(remain // speed)
        else :
            works.append(remain // speed +1)
    delay = works[0]
    idx = 0
    for key, work in enumerate (works):
        if work > delay:
            delay = work
            answer.append(key - idx)
            idx = key
    answer.append(len(works) - idx)
    return answer