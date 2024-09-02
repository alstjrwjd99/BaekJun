import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))

def lis(sequence):
    dp = []
    for num in sequence:
        idx = bisect_left(dp, num)
        if idx == len(dp):
            dp.append(num)
        else:
            dp[idx] = num
    return len(dp)

answer = 0
for i in range(n):
    inc_lis = lis(seq[:i+1])
    dec_lis = lis(reversed(seq[i:]))
    answer = max(answer, inc_lis + dec_lis - 1)

print(answer)