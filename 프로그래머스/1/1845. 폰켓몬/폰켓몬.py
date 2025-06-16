from collections import Counter

def solution(nums):
    c = Counter(nums)
    a = c.values()
    
    if len(nums) // 2 > len(a) :
        return len(a)
    else :
        return len(nums)//2