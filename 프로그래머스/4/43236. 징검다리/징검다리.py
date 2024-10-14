'''
찾아야하는 것 : 바위 거리의 최솟 값 중 가장 큰 값
바위 거리를 mid로 두고 찾기
'''

def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    left, right = 0, distance
    while left <= right :
        mid = (left + right) // 2
        removed = 0
        prev = 0
        for rock in rocks:
            if rock - prev < mid:
                removed += 1
            else :
                prev = rock
            if removed > n:
                break
        if removed > n :
            right = mid - 1
        else :
            left = mid + 1
        
    return left - 1