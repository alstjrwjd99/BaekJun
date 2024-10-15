def solution(n, lost, reserve):
    # 여분이 있지만 도난당한 학생은 자신이 먼저 체육복을 사용하도록 처리
    reserve_only = sorted(set(reserve) - set(lost))  # 여분만 있는 학생
    lost_only = sorted(set(lost) - set(reserve))     # 도난당한 학생 중 여분이 없는 학생

    borrowed = len(lost_only)

    # 여분이 있는 학생들이 체육복을 빌려줌
    for lo in lost_only:
        if (lo - 1) in reserve_only:
            reserve_only.remove(lo - 1)
            borrowed -= 1
        elif (lo + 1) in reserve_only:
            reserve_only.remove(lo + 1)
            borrowed -= 1

    return n - borrowed