def solution(babbling):
    answer = 0
    for word in babbling:
        for pro in ["aya", "ye", "woo", "ma"]:
            if pro * 2 not in word:
                word=word.replace(pro,'1')
        if word.isdigit():
            answer+=1
    return answer