from collections import Counter
def solution(k, tangerine):
    answer = 1
    counter = Counter(tangerine)
    values = sorted(list(counter.values()))
    value_len = len(values)

    max_sum = 0
    for i in range(value_len - 1, -1, -1): 
        max_sum+=values[i]

        if max_sum >=k:
            return answer
        answer += 1


    return answer