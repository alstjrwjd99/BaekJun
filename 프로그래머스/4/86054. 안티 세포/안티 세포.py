MOD = 1_000_000_007

def connect(num, here, par, levels, sum_arr):
    level = levels[here]
    if num not in level:
        level[num] = par

    ret = sum_arr[par]

    if num in levels[par]:
        ret += connect(num * 2, here, levels[par][num], levels, sum_arr)
        ret %= MOD

    return ret


def solution(a, s):
    answer = []
    idx = 0

    for n in s:
        start = idx
        end = start + n
        idx = end

        sum_arr = [0] * (n + 1)
        sum_arr[0] = 1

        levels = [dict() for _ in range(n + 1)]
        levels[0][-1] = -1  # 시작점 표시

        for i in range(1, n + 1):
            sum_arr[i] = connect(a[start + i - 1], i, i - 1, levels, sum_arr) % MOD

        answer.append(sum_arr[n] % MOD)

    return answer