def solution(stones, k):
    def can_cross(stones, k, mid):
        skip = 0
        for stone in stones:
            if stone < mid:
                skip += 1
                if skip >= k:
                    return False
            else:
                skip = 0
        return True
    
    left, right = 1, max(stones)
    
    while left <= right:
        mid = (left + right) // 2
        if can_cross(stones, k, mid):
            left = mid + 1
        else:
            right = mid - 1
    
    return right