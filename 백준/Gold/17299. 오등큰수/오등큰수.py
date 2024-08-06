import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))

from collections import Counter
freq_num = Counter(nums)

answer = [-1] * n

stack = []
for i in range(n-1):
    stack.append((freq_num[nums[i]],i))
    while stack and stack[-1][0] < freq_num[nums[i+1]]:
        val,idx = stack.pop()
        answer[idx] = nums[i+1]
    
print(*answer)