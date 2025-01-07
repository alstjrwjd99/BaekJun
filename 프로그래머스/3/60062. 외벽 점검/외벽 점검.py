from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    weak = weak + [w + n for w in weak]  # 약한 지점을 확장해 원형 문제를 직선처럼 처리
    dist.sort(reverse=True)  # 이동 거리는 내림차순 정렬

    answer = len(dist) + 1  # 초기값: 최대 인원 + 1 (불가능한 경우 대체 값)

    # 각 시작점에 대해 탐색
    for start in range(length):
        # 사람 배치의 모든 순열을 시도
        for friends in permutations(dist):
            count = 1  # 사용할 사람 수
            position = weak[start] + friends[count - 1]  # 첫 사람이 커버할 최대 위치

            # 약한 지점을 순회
            for idx in range(start, start + length):
                if weak[idx] > position:  # 현재 사람으로 커버 불가능한 경우
                    count += 1  # 다음 사람 배치
                    if count > len(friends):  # 더 이상 사람을 배치할 수 없으면 종료
                        break
                    position = weak[idx] + friends[count - 1]  # 다음 사람이 커버할 최대 위치

            # 최소 인원 업데이트
            answer = min(answer, count)

    return answer if answer <= len(dist) else -1