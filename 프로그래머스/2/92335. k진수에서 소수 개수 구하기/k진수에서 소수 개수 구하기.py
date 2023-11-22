def solution(n, k):
    changedNum = ''
    checkPrime = ''
    answer = 0
    while n != 0 :
        changedNum += str(n%k)
        n = n//k     
    changedNum = changedNum[::-1].split('0')
    for i in (changedNum):
        if i != '':
            if isPrime(int(i)):
                answer += 1

    return answer

def isPrime(number):
    if number==1:
        return False
    for i in range(2, int(number**(0.5))+1):
        if number%i==0:
            return False
    return True

