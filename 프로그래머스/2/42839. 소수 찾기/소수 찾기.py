from collections import deque
from copy import deepcopy
import math

def solution(numbers):
    answer = 0
    
    def is_prime(n):
        if n <= 1:
            return False
        for i in range (2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True
    
    def permutation(numbers,goal_length):
        prime_cnt = 0   
        queue = deque([(str(),set())])
        while queue:
            str_num, used_index = queue.popleft()
            for idx,number in enumerate (numbers):
                if idx not in used_index:
                    tmp = str_num + number
                    tmp_idx = deepcopy(used_index)
                    tmp_idx.add(idx)
                    if len(tmp) == goal_length:
                        if int(tmp) not in made and is_prime(int(tmp)):
                            prime_cnt += 1
                            made.add(int(tmp))
                    else :
                        queue.append((tmp,tmp_idx))
        return prime_cnt
    
    made = set()
    for goal_length in range (1, len(numbers)+1):
        answer += permutation(numbers,goal_length)
    return answer