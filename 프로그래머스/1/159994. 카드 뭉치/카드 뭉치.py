def solution(cards1, cards2, goal):
    while goal:
        goal_card = goal.pop(0)
        # 2개가 같다면? -> 다른 단어만 존재한다네요
        if cards1 and goal_card == cards1[0]:
            cards1.pop(0)
        elif cards2 and goal_card == cards2[0]:
            cards2.pop(0)
        else : return 'No'
    return 'Yes'