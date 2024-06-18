from itertools import permutations
import math

def solution(numbers):
    answer = 0
    all_numbers = []
    number_list = []
    for n in numbers:
        number_list.append(n)

    for i in range(1, len(number_list)+1):
        numbers_len_i = list(permutations(number_list, i))
        for j in range(len(numbers_len_i)):
            all_numbers.append(int(''.join(numbers_len_i[j])))

        all_distinct_numbers = set(all_numbers)
        all_distinct_numbers = list(all_distinct_numbers)
        
    for i in range(len(all_distinct_numbers)):
        flag = True
        for j in range(2,int(math.sqrt(all_distinct_numbers[i]))+1):
            if all_distinct_numbers[i] % j == 0:
                flag = False
                break
        if flag == True and all_distinct_numbers[i]!=0  and all_distinct_numbers[i]!=1: 
            answer+=1
    return answer