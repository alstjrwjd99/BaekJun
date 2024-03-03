def solution(number, limit, power):
    answer = []
    # 약수 갯수 구하기
    def getMyDivisor(n):
        divisorsList = []
        for i in range(1, int(n**(1/2)) + 1):
            if (n % i == 0):
                divisorsList.append(i) 
                if ( (i**2) != n) : 
                    divisorsList.append(n // i)
        return len(divisorsList)

    for i in range (1,number+1):
        sword = getMyDivisor(i)
        if sword > limit:
            answer.append(power)
        else:
            answer.append(sword)
    return sum(answer)