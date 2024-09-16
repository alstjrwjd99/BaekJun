import sys
import heapq
from itertools import combinations

input = sys.stdin.readline

# 입력 받기
n, m = map(int, input().split())
city = []
houses = []
chickens = []

# 도시 정보 입력 및 집, 치킨집 위치 저장
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            houses.append((i, j))  # 집 좌표 저장
        elif row[j] == 2:
            chickens.append((i, j))  # 치킨집 좌표 저장
    city.append(row)

# 범위 체크 함수
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 두 좌표 (x1, y1), (x2, y2) 간의 거리 구하기
def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

# 선택된 치킨집 조합에 대해 모든 집의 치킨 거리 계산
def get_chicken_distance(selected_chickens):
    total_distance = 0
    for hx, hy in houses:
        # 각 집에서 가장 가까운 치킨집까지의 거리 찾기
        min_dist = float('inf')
        for cx, cy in selected_chickens:
            min_dist = min(min_dist, distance(hx, hy, cx, cy))
        total_distance += min_dist
    return total_distance

# 치킨집 중 m개를 선택하는 모든 조합에 대해 최소 치킨 거리 구하기
min_chicken_distance = float('inf')
for selected_chickens in combinations(chickens, m):
    min_chicken_distance = min(min_chicken_distance, get_chicken_distance(selected_chickens))

# 결과 출력
print(min_chicken_distance)