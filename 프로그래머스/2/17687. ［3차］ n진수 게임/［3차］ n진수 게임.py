def solution(n, t, m, p):
    
    def n_zinsu(n,num):
        s = ''
        over_ten = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
        while num :
            tmp = num % n 
            if tmp > 9:
                s += over_ten[tmp]
            else :
                s += str(tmp)
            num //= n
        return s[::-1]
    answer = ''    
    total = ''
    num = 0
    while len(total) < t * m:
        total += n_zinsu(n,num)
        num += 1
    total = '0' + total
    time = p
    for i,tube in enumerate(total):
        if i+1 == time:
            answer += tube
            time += m
        if len(answer) == t:
            break
    return answer