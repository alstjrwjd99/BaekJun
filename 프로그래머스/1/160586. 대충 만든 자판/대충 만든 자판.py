from collections import defaultdict

def solution(keymap, targets):
    # 문자 별 최소 누름 횟수 기록
    min_presses = defaultdict(lambda: 1e9)  # 충분히 큰 값으로 초기화
    
    for key in keymap:
        for idx, s in enumerate(key):
            min_presses[s] = min(min_presses[s], idx + 1)
    
    answer = []
    
    # 타겟 문자열 처리
    for target in targets:
        tmp = 0
        for char in target:
            if min_presses[char] == 1e9:  # 해당 문자가 keymap에 없는 경우
                tmp = -1
                break
            else:
                tmp += min_presses[char]
        answer.append(tmp)
    
    return answer