'''
브루트 포스 -> 각 블록의 숫자가 10억 이하의 정수 -> 불가능

이분 탐색 -> 높이 설정 -> 해당 높이를 맞추는 데 드는 값 계산
'''
from bisect import bisect_left
import itertools

def solution(land, P, Q):

    heights = sorted(h for row in land for h in row)
    prefix_sum = list(itertools.accumulate(heights))
    total_blocks = len(heights)
    answer = float('inf')

    unique_heights = sorted(set(heights))

    for h in unique_heights:
        idx = bisect_left(heights, h)

        # h 미만 → 쌓아야 함
        sum_lower = prefix_sum[idx - 1] if idx > 0 else 0
        count_lower = idx
        cost_add = (h * count_lower - sum_lower) * P

        # h 초과 → 깎아야 함
        sum_upper = prefix_sum[-1] - prefix_sum[idx - 1] if idx > 0 else prefix_sum[-1]
        count_upper = total_blocks - idx
        cost_remove = (sum_upper - h * count_upper) * Q

        total_cost = cost_add + cost_remove
        answer = min(answer, total_cost)

    return answer