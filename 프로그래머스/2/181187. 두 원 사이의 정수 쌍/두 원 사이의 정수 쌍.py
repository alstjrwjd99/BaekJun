import math 
def solution(r1, r2):
    answer = 0
    for i in range(1, r2 + 1) :
        answer += math.floor((r2**2 - i**2)**0.5) - math.ceil(max(0,r1**2 - i**2)**0.5) + 1
    return answer*4