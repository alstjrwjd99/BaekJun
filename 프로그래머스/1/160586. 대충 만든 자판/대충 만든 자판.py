def solution(keymap, targets):
    answer = []
    for target in targets:
        ans = 0
        for a in target:
            isFind = False
            press = 101
            for key in keymap:
                if a in key:
                    press = min(press,key.index(a)+1)
                    isFind = True
            if not isFind:
                ans = -1
                break
            ans += press
            
        answer.append(ans)
    return answer