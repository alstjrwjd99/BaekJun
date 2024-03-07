def solution(price, money, count):
    answer = count * price * (count+1)//2 - money
    if answer < 0:
        return 0
    return answer