def solution(numbers, hand):
    answer = ''
    def distance(a,b):
        x = abs((a+2) % 3 - (b+2) % 3)  
        y = abs((a-1)//3 - (b-1) //3)
        return x +y
    left = [1,4,7]
    right = [3,6,9]
    l,r = 10,12
    for num in numbers :
        if num == 0:
            num = 11
        if num in left:
            l = num
            answer += 'L'
        elif num in right :
            r = num
            answer += 'R'
        else :
            if distance(num,r) >distance(num,l):
                l = num
                answer += 'L'
            elif distance(num,r) < distance(num,l):
                r = num
                answer += 'R'
            else :
                if hand == 'right':
                    r = num
                    answer += 'R'
                elif hand =='left':
                    l = num
                    answer += 'L'
    return answer