def solution(arr):
    num=1                   #가장 큰 수에 곱할 숫자
    arr.sort(reverse=True)  #내림차순으로 정렬
    while True:
        temp = arr[0]*num   #배열의 가장 큰 수의 배수   
        count = 0           #공통 배수를 셀 카운트
        for i in arr:
            if temp % i == 0:#temp가 i의 배수라면
                count+=1    #카운트 +1
            else:           #하나라도 배수가 안된다면 for문 종료
                break
        if count == len(arr):#temp가 모든 배열의 수의 배수일 때
            return temp
        num+=1              #곱할 숫자 +1
