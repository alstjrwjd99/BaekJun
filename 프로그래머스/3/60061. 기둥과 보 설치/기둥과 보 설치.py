'''
기둥과 보를 설치 및 삭제할 수 있는 환경인지 체크
있다면 실행 없다면 복구
'''
def solution(n, build_frame):
    made = []
    
    def can_build(x,y,a):
        if a == 0:  # 기둥
            return y == 0 or [x, y - 1, 0] in made or [x - 1, y, 1] in made or [x, y, 1] in made
        else:  # 보
            return ([x, y - 1, 0] in made or [x + 1, y - 1, 0] in made or
                    ([x - 1, y, 1] in made and [x + 1, y, 1] in made))
    
    def is_valid_structure():
        for x, y, a in made:
            if not can_build(x, y, a):
                return False
        return True

    for x,y,a,b in build_frame:
        # 삭제
        if b == 0 :
            made.remove([x,y,a])
            if not is_valid_structure():
                made.append([x,y,a])
        # 설치
        if b == 1 :
            made.append([x,y,a])
            if not is_valid_structure():
                made.remove([x,y,a])

    return sorted(made, key = lambda x : (x[0], x[1], x[2]))