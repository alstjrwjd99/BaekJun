import sys
input = sys.stdin.readline

n,m = map(int,input().split())
nums = list(map(int,input().split()))

for i in range (1,n):
  nums[i] = nums[i] + nums[i-1]

for _ in range (m):
  start, end = map(int,input().split())
  if start == 1 :
    print(nums[end-1])
  else :
    print(nums[end-1]-nums[start-2])