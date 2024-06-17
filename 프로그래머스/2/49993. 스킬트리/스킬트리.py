def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        pointer = 0
        is_answer = True
        for sk in skill_tree:
            if sk in skill:
                if pointer < skill.index(sk):
                    is_answer = False
                    break
                else :
                    pointer += 1
        if is_answer :
            answer += 1
    return answer