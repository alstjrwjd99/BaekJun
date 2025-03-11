import sys
input = sys.stdin.readline
from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))

dp = []            # LIS의 길이를 구하기 위한 배열
trace = [-1] * n   # LIS 수열 복원을 위한 추적 배열
lis_index = [-1] * n   # LIS 원소의 위치를 저장하는 배열

for i in range(n):
    idx = bisect_left(dp, arr[i])
    if idx >= len(dp):  # LIS 배열의 끝에 추가
        dp.append(arr[i])
        lis_index[idx] = i  # LIS 위치 저장
    else:
        dp[idx] = arr[i]    # 더 작은 값으로 대체해 LIS 길이 유지
        lis_index[idx] = i  # LIS 위치 갱신
    
    # 이전 원소의 위치 추적
    if idx == 0:
        trace[i] = -1  # LIS의 첫 번째 원소
    else:
        trace[i] = lis_index[idx - 1]  # 이전 위치 저장

# LIS의 길이 출력
print(len(dp))

# LIS 수열 복원
lis = []
idx = lis_index[len(dp) - 1]  # 마지막 LIS 위치부터 역추적
while idx != -1:
    lis.append(arr[idx])
    idx = trace[idx]

# 결과 출력 (LIS는 역순이므로 뒤집기)
print(*reversed(lis))