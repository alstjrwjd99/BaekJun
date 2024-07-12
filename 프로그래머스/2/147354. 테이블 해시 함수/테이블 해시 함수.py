def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key = lambda x : (x[col-1],-x[0]))

    for i in range (row_begin-1, row_end):
        tmp = 0
        for d in data[i]:
            tmp += d % (i+1)
        answer ^= tmp
    return answer