from collections import Counter

def solution(a):
    if len(a) < 2:  
        return 0
    
    counter = Counter(a)
    max_length = 0

    for key in counter:
        if counter[key] * 2 <= max_length:
            continue
        length = 0
        i = 0
        while i < len(a) - 1:
            if (a[i] == key or a[i+1] == key) and a[i] != a[i+1]:
                length += 2
                i += 2 
            else:
                i += 1 
        
        max_length = max(max_length, length) 

    return max_length