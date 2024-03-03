def solution(food):
    answer = ''
    for idx,fo in enumerate (food):
        if fo != 0:
            answer+=(str(idx) * (fo//2))
    answer = answer + '0' + (answer[::-1])
    return answer