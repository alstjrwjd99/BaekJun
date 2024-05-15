'''
0,1이 바뀌면 수정을 해야함
1. O(N)으로 비교하며 풀면 됨
'''
T = int(input())

for test_case in range(1, T+1):
    bits = input().rstrip()
    ans = 0
    flag = '0'
    for bit in bits:
        if bit != flag:
            ans += 1
            flag = bit
    print(f'#{test_case} {ans}')
