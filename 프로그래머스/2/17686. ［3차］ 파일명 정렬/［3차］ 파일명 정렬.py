'''
1. head, number 분리
head, number로 나누고 나머지는 버리면 된다
head는 string -> 숫자 나오기 전까지
number는 int -> isdigit() -> 5글자 제한이 있네
tail은 숫자 뒤에 오는 문자

2. 정렬
2-1. head 기준 사전 순 정렬 대소문자 구분안함
2-2. head가 동일 -> number순 정렬
2-3. 둘다 동일 -> 입력순 -> input()에서 index를 같이 저장
'''
def solution(files):
    answer = []
    # Step1 분류
    classify = []
    for idx, file in enumerate(files):
        head = ''
        number = ''
        isTail = False
        number_limit = 0
        for name in file:
            if number_limit <= 5 and name.isdigit():
                number += name
                number_limit += 1
                isTail = True
            else :
                if isTail : 
                    break
                head += name
        classify.append((head.lower(),int(number),idx))

    # Step2 정렬
    classify.sort(key = lambda x : (x[0],x[1],x[2]))
    for c in classify:
        answer.append(files[c[2]])
    return answer