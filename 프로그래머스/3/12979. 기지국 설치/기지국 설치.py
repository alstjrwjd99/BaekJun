import math

def solution(n, stations, w):
    answer = 0
    start = 0
    for station in stations:
        if start < station -w-1:
            print(station-w-1 - start)
            answer += math.ceil((station-w-1 - start) / (2*w + 1) )
        start = station + w 
    if stations[-1] + w < n:
        answer += math.ceil((n - stations[-1] - w ) / (2*w + 1) )
    return answer