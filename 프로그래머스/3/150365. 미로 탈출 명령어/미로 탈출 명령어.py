def solution(n, m, x, y, r, c, k):
    # 좌상단이 (1, 1), 우하단이 (n, m)이고 초기 위치는 (x, y) -> 목적지 (r, c)
    diff = abs(x - r) + abs(y - c)
    
    # 이동이 불가능한 경우
    if diff > k or (diff % 2 != k % 2):
        return "impossible"

    # dlru 순으로 이동량 계산
    rest = k - diff
    dcount, ucount, lcount, rcount = 0, 0, 0, 0

    if x < r:
        dcount = r - x  # 아래로 내려가기
    else:
        ucount = x - r  # 위로 올라가기

    if y < c:
        rcount = c - y  # 오른쪽으로 이동
    else:
        lcount = y - c  # 왼쪽으로 이동

    # 추가 이동량 분배
    dplus = min(n - max(x, r), rest // 2)  # 남은 아래로 이동 가능한 범위
    rest -= dplus * 2

    lplus = min(min(y, c) - 1, rest // 2)  # 남은 왼쪽으로 이동 가능한 범위
    rest -= lplus * 2

    # 경로 생성
    answer = (
        "d" * (dcount + dplus) +
        "l" * (lcount + lplus) +
        "rl" * (rest // 2) +
        "r" * (rcount + lplus) +
        "u" * (ucount + dplus)
    )

    return answer