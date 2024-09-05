import sys
input = sys.stdin.read

numbers = input().splitlines()

def kantor(n, idx):
    if n == 1:
        line[idx] = '-'
        return
    
    # 현재 구간의 길이와 중간 구간의 시작 위치를 계산
    segment_length = n // 3
    
    # 왼쪽과 오른쪽 구간을 '-'로 설정
    kantor(segment_length, idx)
    kantor(segment_length, idx + 2 * segment_length)


for n in numbers:
    n = int(n)
    length = 3**n
    line = [' '] * length

    kantor(length, 0)
    print(''.join(line))