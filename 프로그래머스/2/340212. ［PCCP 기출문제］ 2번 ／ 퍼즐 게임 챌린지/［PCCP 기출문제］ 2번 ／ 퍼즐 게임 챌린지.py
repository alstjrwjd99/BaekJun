def solution(diffs, times, limit):
    def can_complete(level):
        total_time = 0
        for i in range(len(diffs)):
            if diffs[i] <= level:
                total_time += times[i]
            else:
                total_time += (diffs[i] - level) * (times[i] + (times[i - 1] if i > 0 else 0)) + times[i]
            if total_time > limit:
                return False
        return True

    left, right = 1, max(diffs)
    answer = right

    while left <= right:
        mid = (left + right) // 2
        if can_complete(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer