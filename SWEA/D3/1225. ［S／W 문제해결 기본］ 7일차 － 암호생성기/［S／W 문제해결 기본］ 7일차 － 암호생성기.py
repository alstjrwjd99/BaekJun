'''
싸이클 돌리면서 무식하게 하면 될듯
'''
from collections import deque

T = 10

for test_case in range(1,T+1):
    tc = int(input())
    nums = list(map(int,input().split()))
    queue = deque(nums)
    flag = True
    while flag:
        for i in range(1, 6):
            x = queue.popleft()
            zero_test = x - i
            if zero_test <= 0:
                flag = False
                queue.append(0)
                break

            queue.append(zero_test)

    print(f'#{test_case}')
    for i in queue:
        print(i,end=' ')

