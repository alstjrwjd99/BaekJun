import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        least = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, least + second * 2)
        answer += 1
        if len(scoville) < 2 and scoville[0] < K:
            return -1
    return answer