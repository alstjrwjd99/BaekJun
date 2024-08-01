from functools import cmp_to_key

def solution(numbers):
    answer = ''
    # 두 숫자를 바꿔야하는지 여부
    def to_swap(x,y):
        if str(y)+str(x)>=str(x)+str(y) : return 1
        else : return -1
    numbers.sort(key = cmp_to_key(to_swap))
    return str(int(''.join(map(str,numbers)))) # [0,0]이 주어지는 경우 대비해서 str(int())

                 