def solution(n, build_frame):
    made = []
    
    # 구조물이 조건을 만족하는지 확인
    def can_build(x, y, a):
        if a == 0:  # 기둥
            return y == 0 or \
                   [x, y - 1, 0] in made or \
                   [x - 1, y, 1] in made or \
                   [x, y, 1] in made
        else:  # 보
            return ([x, y - 1, 0] in made or [x + 1, y - 1, 0] in made or
                    ([x - 1, y, 1] in made and [x + 1, y, 1] in made))

    # 현재 상태가 조건을 만족하는지 확인
    def is_valid_structure():
        for x, y, a in made:
            if not can_build(x, y, a):
                return False
        return True

    for x, y, a, b in build_frame:
        if b == 1:  # 설치
            made.append([x, y, a])
            if not is_valid_structure():  # 조건을 만족하지 않으면 되돌리기
                made.remove([x, y, a])
        else:  # 삭제
            made.remove([x, y, a])
            if not is_valid_structure():  # 조건을 만족하지 않으면 복구
                made.append([x, y, a])

    return sorted(made, key=lambda x: (x[0], x[1], x[2]))