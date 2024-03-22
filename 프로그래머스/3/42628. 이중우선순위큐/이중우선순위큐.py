import heapq

def solution(operations):
    answer = []
    heap = []
    
    for oper in operations:
        op, value = oper.split()
        
        if op == "I":
            heapq.heappush(heap, int(value))
        elif op == "D":
            if heap:
                if value == '-1':
                    heapq.heappop(heap)  # 최소값을 제거
                else:
                    heap.remove(max(heap))  # 최대값을 제거
                    heapq.heapify(heap)  # 힙 속성 재정렬    
    if heap:
        answer.append(max(heap))
        answer.append(min(heap))
    else :
        answer.append(0)
        answer.append(0)
    return answer
