import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1  # 모든 음식을 다 먹을 수 없음
    
    # 우선순위 큐 (음식 시간, 인덱스)
    heap = []
    for i, time in enumerate(food_times):
        heapq.heappush(heap, (time, i + 1))  # (시간, 인덱스)
    
    total_time = 0
    prev_time = 0
    food_count = len(food_times)
    
    while heap:
        # 현재 음식의 최소 시간
        time, index = heap[0]
        # 현재 레벨에서 한 바퀴 도는데 걸리는 시간
        cycle_time = (time - prev_time) * food_count
        
        if total_time + cycle_time > k:
            break  # 남은 시간(k)이 부족하면 멈춤
        
        total_time += cycle_time
        prev_time = heapq.heappop(heap)[0]  # 먹은 음식 제거
        food_count -= 1  # 음식 개수 줄임
    
    # 남은 음식들에서 결과 반환
    remaining_foods = sorted(heap, key=lambda x: x[1])  # 인덱스로 정렬
    return remaining_foods[(k - total_time) % food_count][1]