def solution(name):
    answer = 0

    def updown(alpha):
        return min(ord(alpha) - ord('A'), ord('Z') - ord(alpha) + 1)

    goal_move = [updown(i) for i in name]
    answer += sum(goal_move)

    # 좌/우 이동 횟수 계산
    n = len(name)
    min_move = n - 1  # 일단 오른쪽 끝까지 쭉 가는 경우로 초기화

    for i in range(n):
        next_pos = i + 1
        # 연속된 'A'를 넘어간 다음 위치를 찾음
        while next_pos < n and name[next_pos] == 'A':
            next_pos += 1

        # i에서 시작하여 오른쪽으로 가고, 다시 돌아가서 왼쪽으로 돌아오는 경로를 계산
        min_move = min(min_move, i + n - next_pos + min(i, n - next_pos))

    answer += min_move
    return answer