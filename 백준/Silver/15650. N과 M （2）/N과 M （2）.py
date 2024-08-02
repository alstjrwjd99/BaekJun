import sys
input = sys.stdin.readline

n,m = map(int,input().split())

def dfs(nums,start):
    if len(nums) == m:
        print(*nums)
        return 

    for i in range (start,n+1):
        nums.append(i)
        dfs(nums,i+1)
        nums.pop()
        

dfs([],1)