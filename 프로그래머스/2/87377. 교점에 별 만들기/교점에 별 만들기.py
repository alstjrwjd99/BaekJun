from itertools import combinations

def find_xy(a, b, c, d, e, f):
    denominator = a * d - b * c
    if denominator == 0:
        return None
    x_numerator = b * f - e * d
    y_numerator = e * c - a * f
    if x_numerator % denominator == 0 and y_numerator % denominator == 0:
        return (x_numerator // denominator, y_numerator // denominator)
    return None

def solution(line):
    coors = set()
    
    # 교점 구하기
    for combi in combinations(line, 2):
        a, b, e = combi[0]
        c, d, f = combi[1]
        result = find_xy(a, b, c, d, e, f)
        if result:
            coors.add(result)
    
    if not coors:
        return []
    
    # 최대, 최소 좌표 계산
    min_x = min(x for x, y in coors)
    max_x = max(x for x, y in coors)
    min_y = min(y for x, y in coors)
    max_y = max(y for x, y in coors)

    # 결과 배열 생성
    result = []
    for y in range(max_y, min_y - 1, -1):  # y는 위에서 아래로
        row = ''
        for x in range(min_x, max_x + 1):  # x는 왼쪽에서 오른쪽으로
            if (x, y) in coors:
                row += '*'
            else:
                row += '.'
        result.append(row)
    
    return result