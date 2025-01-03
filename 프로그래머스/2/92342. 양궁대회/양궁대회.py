'''
라이언이 점수를 얻을 수 있는 경우
1. 어피치랑 같은 점수를 쐈을 때
    - 더 많이 맞추면 됨 ( 같으면 안됨 )
2. 어피치랑 다른 점수를 쐈을 때
    - 한번만 맞추면 됨

가장 큰 점수 차이로 우승해야함
-> 어치피의 점수를 많이 뻇어오는 경우
-> 그냥 최고 득점 하는 경우

백트래킹 완전탐색
10점 -> 0점 순서대로 진행
'''
def solution(n, info):
    answer = [-1] * 11
    max_diff = 0 

    def calculate_score(ryan, apeach):
        ryan_score, apeach_score = 0, 0
        for i in range(11):
            if ryan[i] > info[i]:  # 라이언이 점수를 가져가는 경우
                ryan_score += 10 - i
            elif info[i] > 0:  # 어피치가 점수를 가져가는 경우
                apeach_score += 10 - i
        return ryan_score, apeach_score

    def dfs(idx, arrows_left, ryan):
        nonlocal answer, max_diff

        if idx == 11 or arrows_left == 0:  # 모든 과녁을 탐색했거나 화살이 없는 경우
            if arrows_left > 0:  # 남은 화살을 0점에 모두 쏘기
                ryan[10] += arrows_left

            ryan_score, apeach_score = calculate_score(ryan, info)
            score_diff = ryan_score - apeach_score

            if score_diff > max_diff:  # 더 큰 점수 차이를 발견한 경우
                max_diff = score_diff
                answer = ryan[:]
            elif score_diff == max_diff:  # 점수 차이가 같을 경우 낮은 점수를 더 많이 맞힌 배열 선택
                for i in range(10, -1, -1):
                    if ryan[i] > answer[i]:
                        answer = ryan[:]
                        break
                    elif ryan[i] < answer[i]:
                        break

            if arrows_left > 0:  # 남은 화살을 복구
                ryan[10] -= arrows_left

            return

        # 어피치보다 하나 더 쏘는 경우 (가능하면)
        if arrows_left > info[idx]:
            ryan[idx] = info[idx] + 1
            dfs(idx + 1, arrows_left - (info[idx] + 1), ryan)
            ryan[idx] = 0  

        # 화살을 쏘지 않는 경우
        dfs(idx + 1, arrows_left, ryan)

    dfs(0, n, [0] * 11) 

    return answer if max_diff > 0 else [-1]