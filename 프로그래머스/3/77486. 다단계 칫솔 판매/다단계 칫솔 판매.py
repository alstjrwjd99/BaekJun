def solution(enroll, referral, seller, amount):
    tree = {"-": [None, 0]}
    for en, re in zip(enroll, referral):
        tree[en] = [re, 0]
    
    for name, cnt in zip(seller, amount):
        earnings = cnt * 100
        while name != "-":
            up_share = earnings // 10
            tree[name][1] += earnings - up_share
            if up_share == 0:
                break
            name = tree[name][0]
            earnings = up_share

    return [tree[name][1] for name in enroll]