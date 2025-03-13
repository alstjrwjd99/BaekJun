import sys
input = sys.stdin.readline

while True:
    data = list(map(int, input().split()))
    if data[0] == 0:
        break

    # 첫 번째 숫자는 막대의 개수이므로 제외하고, 실제 높이 리스트를 사용
    n = data[0]
    rect = data[1:]
    rect.append(0)
    stack = []
    answer = 0

    for i in range(len(rect)):
        while stack and rect[i] < rect[stack[-1]]:
            h = rect[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            answer = max(answer, h * w)
        stack.append(i)

    print(answer)