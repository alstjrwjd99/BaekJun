import sys
import heapq

input = sys.stdin.readline

# 입력 처리
N, K = map(int, input().split())
gems = []
bags = []

# 보석 정보 입력 (무게, 가치)
for _ in range(N):
    weight, value = map(int, input().split())
    gems.append((weight, value))

# 가방 정보 입력
for _ in range(K):
    bags.append(int(input()))

# 보석과 가방을 무게 기준으로 오름차순 정렬
gems.sort()
bags.sort()

# 우선순위 큐 (최대 힙) 준비
max_heap = []
answer = 0
gem_index = 0

# 각 가방에 대해 담을 수 있는 보석 중 가장 높은 가치를 선택
for bag in bags:
    # 현재 가방의 무게를 담을 수 있는 보석들 추가
    while gem_index < N and gems[gem_index][0] <= bag:
        # 가치 기준 최대 힙을 위해 -value를 사용
        heapq.heappush(max_heap, -gems[gem_index][1])
        gem_index += 1
    
    # 가방에 담을 수 있는 가장 큰 가치를 선택
    if max_heap:
        answer -= heapq.heappop(max_heap)

print(answer)