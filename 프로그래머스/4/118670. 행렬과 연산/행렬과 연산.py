from collections import deque

def solution(rc, operations):
    r, c = len(rc), len(rc[0])
    L = deque(rc[i][0] for i in range(r))
    R = deque(rc[i][c-1] for i in range(r))
    M = deque(deque(rc[i][1:c-1]) for i in range(r))

    def apply_shift(k):
        if k % r == 0: return
        L.rotate(k); R.rotate(k); M.rotate(k)

    shift = 0
    for op in operations:
        if op == "ShiftRow":
            shift += 1
        else:  # "Rotate"
            apply_shift(shift); shift = 0
            if c == 1:  # only one column, rotate is no-op
                continue
            if c == 2:
                # middle empty: move between L and R only
                R.appendleft(L.popleft())
                L.append(R.pop())
            else:
                x = L.popleft(); M[0].appendleft(x)
                x = M[0].pop();  R.appendleft(x)
                x = R.pop();     M[-1].append(x)
                x = M[-1].popleft(); L.append(x)

    apply_shift(shift)

    # rebuild
    res = []
    for i in range(r):
        row = [L[i]]
        if c > 2: row += list(M[i])
        if c > 1: row += [R[i]]
        res.append(row)
    return res