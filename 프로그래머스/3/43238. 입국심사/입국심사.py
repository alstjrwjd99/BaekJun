def solution(n, times):
    left, right = 1, max(times) * n  # 최소 1분, 최대 시간은 가장 긴 심사관이 모두 처리할 경우
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        judge_member = 0
        
        # mid 시간 동안 심사할 수 있는 인원 수 계산
        for time in times:
            judge_member += mid // time
        
        if judge_member >= n:
            # 가능한 경우, 더 작은 시간을 찾아본다
            answer = mid
            right = mid - 1
        else:
            # 심사 인원이 부족한 경우, 시간을 더 늘려야 한다
            left = mid + 1
    
    return answer