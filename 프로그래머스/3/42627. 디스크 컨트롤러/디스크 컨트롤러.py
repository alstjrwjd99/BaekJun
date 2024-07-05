import heapq

def solution(jobs):
    answer = 0
    hq = []
    i,now = 0,0
    start = -1
    
    while i <len(jobs):
        for job in jobs:
            if start< job[0] <= now:
                heapq.heappush(hq,[job[1],job[0]])
        if len(hq) > 0:
            current = heapq.heappop(hq)
            start = now
            now += current[0]
            answer += (now - current[1])
            i+=1
        else:
            now += 1
    return answer//len(jobs)