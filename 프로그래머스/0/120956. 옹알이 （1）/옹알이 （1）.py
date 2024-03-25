def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]
    for i in range(len(babbling)):
        for word in words:
            babbling[i] = babbling[i].replace(word, ' ')
        babbling[i] = babbling[i].replace(' ', '')
    return babbling.count('')