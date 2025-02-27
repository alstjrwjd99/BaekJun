import sys
input = sys.stdin.readline
from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))
stack = []
tmp = []
for i in arr:
    if not stack or stack[-1] < i:
        stack.append(i)
        tmp.append((len(stack)-1, i))
    else:
        stack[bisect_left(stack, i)] = i
        tmp.append((bisect_left(stack, i), i))

ans = []
last_idx = len(stack)-1
for i in range(len(tmp)-1, -1, -1):
    if tmp[i][0] == last_idx:
        ans.append(tmp[i][1])
        last_idx -= 1

print(len(stack))
print(*ans[::-1])