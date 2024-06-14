'''
heap을 이용해서 풀어보자
'''
import heapq

def solution(n, works):
    answer = 0
    hq = []
    for work in works:
        heapq.heappush(hq,(-1)*work)
    while n != 0:
        n -= 1
        max_work = heapq.heappop(hq)
        if max_work < -1:
            heapq.heappush(hq,max_work+1)
        if len(hq) == 0 : return 0
    for wo in hq:
        answer += wo ** 2
    return answer