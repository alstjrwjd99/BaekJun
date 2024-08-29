def solution(lottos, win_nums):
    cnt,zero = 0,0
    for lotto in lottos:
        if lotto in set(win_nums) : cnt += 1
        elif lotto == 0 : zero += 1
    return [6 if cnt+zero == 0 else 7 - cnt-zero,6 if cnt == 0 else 7-cnt]