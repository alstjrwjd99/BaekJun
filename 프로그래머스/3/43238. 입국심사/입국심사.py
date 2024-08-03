def solution(n, times):
    left = 1
    right = max(times) * n
    
    while left < right:
        mid = left + (right - left) // 2
        done = 0
        
        for time in times:
            done += mid // time
        
        if done >= n:
            right = mid
        else:
            left = mid + 1
    
    return left