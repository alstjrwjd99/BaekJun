import heapq

def solution(scoville, K):
    answer = 0
    hq = []
    for degree in scoville:
        heapq.heappush(hq,degree)
        
    while len(hq)>1 and hq[0] < K :
        one = heapq.heappop(hq)
        two = heapq.heappop(hq)
        heapq.heappush(hq, (one + two * 2))
        answer += 1
    
    if hq[0] < K : return -1
    return answer