def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries = [0] + deliveries
    pickups = [0] + pickups

    # 먼 거리부터 순회하는 전략이므로 역순으로 간편하게 처리
    far_deliveries = n  # 배달할 가장 먼 지점
    far_pickups = n     # 수거할 가장 먼 지점

    while far_deliveries > 0 or far_pickups > 0:
        # 배달의 먼 지점을 탐색
        while far_deliveries > 0 and deliveries[far_deliveries] == 0:
            far_deliveries -= 1

        # 수거의 먼 지점을 탐색
        while far_pickups > 0 and pickups[far_pickups] == 0:
            far_pickups -= 1

        # 가장 먼 거리 계산
        farthest = max(far_deliveries, far_pickups)

        # 한 번의 왕복 거리 추가
        answer += farthest * 2

        # 현재 남은 용량
        remain_cap = cap

        # 배달을 진행
        for i in range(far_deliveries, 0, -1):
            if deliveries[i] > 0:
                if deliveries[i] <= remain_cap:
                    remain_cap -= deliveries[i]
                    deliveries[i] = 0
                else:
                    deliveries[i] -= remain_cap
                    remain_cap = 0

                # 용량이 모두 찼다면 멈춤
                if remain_cap == 0:
                    break

        # 수거를 진행
        remain_cap = cap  # 배달 용량 초기화
        for i in range(far_pickups, 0, -1):
            if pickups[i] > 0:
                if pickups[i] <= remain_cap:
                    remain_cap -= pickups[i]
                    pickups[i] = 0
                else:
                    pickups[i] -= remain_cap
                    remain_cap = 0

                # 용량이 모두 찼다면 멈춤
                if remain_cap == 0:
                    break

    return answer