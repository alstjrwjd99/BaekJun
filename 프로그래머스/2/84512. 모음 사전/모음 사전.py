def solution(word):
    global answer, count
    answer = 0
    count = 0
    vowels = ['A', 'E', 'I', 'O', 'U']  # 사용할 모음들

    def dfs(made):
        global answer, count

        # 매번 호출 시 카운트를 증가시키고, 원하는 단어와 일치하는지 확인
        count += 1
        if made == word:
            answer = count
            return True  # 찾았을 경우 True를 반환하여 종료

        # made가 길이가 5 이상이면 더 이상 추가하지 않음
        if len(made) == 5:
            return False

        # A, E, I, O, U를 각각 재귀적으로 추가
        for vowel in vowels:
            if dfs(made + vowel):  # 새로운 문자를 추가하고, 재귀 호출
                return True
        return False

    # 빈 문자열로 시작하여 탐색 시작
    dfs("")
    return answer-1