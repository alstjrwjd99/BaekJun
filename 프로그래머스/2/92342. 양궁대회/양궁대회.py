def solution(n, info):
    answer = [-1] * 11  # 결과 저장
    max_diff = 0  # 최대 점수 차이 저장

    # 점수 계산 함수
    def calculate_score(ryan, apeach):
        ryan_score, apeach_score = 0, 0
        for i in range(11):
            if ryan[i] > info[i]:  # 라이언이 점수를 가져가는 경우
                ryan_score += 10 - i
            elif info[i] > 0:  # 어피치가 점수를 가져가는 경우
                apeach_score += 10 - i
        return ryan_score, apeach_score

    # DFS 탐색
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
            ryan[idx] = 0  # 백트래킹

        # 화살을 쏘지 않는 경우
        dfs(idx + 1, arrows_left, ryan)

    dfs(0, n, [0] * 11)  # 초기화 상태로 DFS 시작

    return answer if max_diff > 0 else [-1]