def solution(a, b, g, s, w, t):
    start = 0
    end = (10**9) * (10**5) * 4
    answer = end

    while start <= end:
        mid = (start + end) // 2
        total_gold, total_silver, total_material = 0, 0, 0

        for now_gold, now_silver, now_weight , now_time in zip(g,s,w,t):
            move_cnt = mid // (now_time * 2)
            if mid % (now_time * 2) >= now_time: 
                move_cnt += 1

            carry_gold = min(move_cnt * now_weight, now_gold)
            carry_silver = min(move_cnt * now_weight, now_silver)
            carry_total = min(move_cnt * now_weight, now_gold + now_silver)

            total_gold += carry_gold
            total_silver += carry_silver
            total_material += carry_total

        if total_gold >= a and total_silver >= b and total_material >= a + b:
            answer = mid 
            end = mid - 1 
        else:
            start = mid + 1 

    return answer