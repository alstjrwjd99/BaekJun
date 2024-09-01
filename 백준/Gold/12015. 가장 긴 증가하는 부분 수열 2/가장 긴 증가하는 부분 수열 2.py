import sys
input = sys.stdin.readline

import bisect

N = int(input())
A = list(map(int,input().split()))

dp = [0]

for i in A:
  idx = bisect.bisect_left(dp,i)
  if idx == len(dp):
    dp.append(i)
  else:
    dp[idx] = i

print(len(dp)-1)  