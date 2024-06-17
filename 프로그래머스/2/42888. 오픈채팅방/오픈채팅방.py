def solution(record):
    answer = []
    open_kakao = dict()
    for msg in record:
        tmp = msg.split()
        if tmp[0] == 'Enter':
            answer.append([tmp[1],'님이 들어왔습니다.'])
            open_kakao[tmp[1]] = tmp[2]
        elif tmp[0] == 'Leave':
            answer.append([tmp[1],'님이 나갔습니다.'])
        else:
            open_kakao[tmp[1]] = tmp[2]
    for idx,ans in enumerate(answer):
        if ans[0] in open_kakao:
            answer[idx] = open_kakao[ans[0]] + ans[1]
    return answer