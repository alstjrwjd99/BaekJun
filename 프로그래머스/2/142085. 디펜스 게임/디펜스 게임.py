import heapq

def solution(n, k, enemy):
    answer = 0

    pq = []

    for i in range(len(enemy)):        
        if n >= enemy[i]:
            n -= enemy[i]
            heapq.heappush(pq, (-enemy[i], enemy[i]))
        elif k > 0:
                if pq and enemy[i] <= pq[0][1]:
                    n += (heapq.heappop(pq)[1] - enemy[i])
                    heapq.heappush(pq, (-enemy[i], enemy[i]))
                k -= 1
        else:
            answer = i
            break
        answer = i+1
    return answer