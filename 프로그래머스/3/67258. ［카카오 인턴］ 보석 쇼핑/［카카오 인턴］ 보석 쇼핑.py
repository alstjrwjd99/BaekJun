def solution(gems):
    gem = list(set(gems))
    n = len(gem)
    
    dic = {gems[0]: 1}
    answer = [1, len(gems)]
    left,right = 0,0
    while left <= right and right < len(gems):
        if len(dic) == n:
            if answer[1]-answer[0] > right-left:
                answer = [left+1, right+1]
            
            dic[gems[left]] -= 1
            if dic[gems[left]] == 0:
                del dic[gems[left]]
            left += 1

        elif len(dic) < n:
            right += 1
            if right >= len(gems):
                break
            if gems[right] not in dic:
                dic[gems[right]] = 1
            else:
                dic[gems[right]] += 1
        
    return answer