function solution(rsp) {
    var answer = '';
    const win = {'2': '0', '0': '5', '5': '2'};
    answer = rsp.split('').map(s => win[s]).join('');
    return answer;
}