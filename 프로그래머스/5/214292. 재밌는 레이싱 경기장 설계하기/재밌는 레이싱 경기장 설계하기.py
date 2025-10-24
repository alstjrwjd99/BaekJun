def solution(heights):
    heights.sort()
    minusV = []
    n = len(heights)

    if n % 2 == 1:
        for i in range(n // 2):
            minusV.append(heights[i + n // 2] - heights[i])
        minusV.append(heights[-1] - heights[n // 2])
        minusV.sort()
        return minusV[1]
    else:
        for i in range(n // 2):
            minusV.append(heights[i + n // 2] - heights[i])
        minusV.sort()
        return minusV[0]