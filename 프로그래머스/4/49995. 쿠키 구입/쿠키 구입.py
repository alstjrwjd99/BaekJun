def solution(cookie):
    answer = 0
    n = len(cookie)

    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + cookie[i - 1]

    for mid in range(1, n):
        left, right = mid, mid + 1 
        while left > 0 and right <= n:  
            left_sum = prefix_sum[mid] - prefix_sum[left - 1] 
            right_sum = prefix_sum[right] - prefix_sum[mid] 

            if left_sum == right_sum:
                answer = max(answer, left_sum)
                left -= 1
                right += 1
            elif left_sum < right_sum:  # 오른쪽이 더 크면 왼쪽 확장
                left -= 1
            else:  # 왼쪽이 더 크면 오른쪽 확장
                right += 1

    return answer