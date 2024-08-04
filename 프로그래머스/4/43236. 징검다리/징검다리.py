def solution(distance, rocks, n):
    rocks.sort()
    left = 1
    right = distance
    rocks.append(distance)
    
    while left <= right:
        mid = (left + (right-left)//2)
        prev = 0
        removed = 0
        
        for rock in rocks:
            if rock - prev < mid:
                removed += 1
            else:
                prev = rock
            if removed > n:
                break

        if removed > n:
            right = mid - 1
        else:
            left = mid + 1

    return left-1