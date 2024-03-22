def solution(elements):
    answer = 0
    sumcnt = set()
    n = len(elements)
    elements = elements + elements
    print(elements)
    for i in range (n):
        for j in range (n):
            sumcnt.add(sum(elements[i:i+j]))
    return len(sumcnt)