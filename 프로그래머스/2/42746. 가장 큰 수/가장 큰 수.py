from functools import cmp_to_key

def solution(numbers):
    # 두 숫자를 바꿔야하는지 여부
    def to_swap(x,y):
        if str(y)+str(x)>=str(x)+str(y) : return 1
        else : return -1
    numbers.sort(key = cmp_to_key(to_swap))
    answer = ''.join(map(str,numbers))
    return "0" if answer[0] == "0" else answer
                 