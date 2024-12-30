def solution(key, lock):
    n = len(lock)
    m = len(key)

    # 자물쇠의 크기를 확장해서 그리드 생성
    def create_extended_lock(lock):
        size = n + 2 * m
        extended_lock = [[0] * size for _ in range(size)]
        # 확장된 그리드에 자물쇠를 복사
        for i in range(n):
            for j in range(n):
                extended_lock[i + m][j + m] = lock[i][j]
        return extended_lock

    # 열쇠 회전 함수
    def rotate_key(key):
        return [[key[m - 1 - j][i] for j in range(m)] for i in range(m)]

    # 자물쇠와 열쇠가 맞는지 확인
    def check(extended_lock, key, start_x, start_y):
        size = n + 2 * m
        temp_lock = [row[:] for row in extended_lock]  # 임시 자물쇠 배열 복사

        # 열쇠를 덧댐
        for i in range(m):
            for j in range(m):
                temp_lock[start_x + i][start_y + j] += key[i][j]

        # 자물쇠 영역이 모두 1인지 체크
        for i in range(m, m + n):
            for j in range(m, m + n):
                if temp_lock[i][j] != 1:  # 1이 아니면 실패
                    return False
        return True

    # 확장된 자물쇠 그리드 생성
    extended_lock = create_extended_lock(lock)

    # 모든 경우에 대해 확인
    for _ in range(4):  # 열쇠를 4번 회전하며 확인
        for x in range(1, n + m):
            for y in range(1, n + m):
                if check(extended_lock, key, x, y):
                    return True
        key = rotate_key(key)  # 열쇠 회전

    return False