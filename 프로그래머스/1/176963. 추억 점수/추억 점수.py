def solution(name, yearning, photo):
    answer = []
    for pho in photo:
        ans = 0
        print('-----------')
        print(pho)
        for na in name :
            if na in pho:
                print(na)
                print(name.index(na))
                print(yearning[name.index(na)])
                ans += yearning[name.index(na)]
        answer.append(ans)
    return answer