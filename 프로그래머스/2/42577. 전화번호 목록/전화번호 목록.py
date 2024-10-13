def solution(phone_book):
    answer = True
    phone_numbers = set(phone_book)
    for phone_number in phone_numbers:
        temp = ''
        for number in phone_number:
            temp += number
            if temp in phone_numbers and temp != phone_number:
                answer = False
    return answer