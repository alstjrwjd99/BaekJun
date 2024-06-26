function solution(l, r) {
    var answer = [];
    for (let i = l ; i <= r; i++){
        if (String(i).replaceAll('5','').replaceAll('0','').length === 0){
            answer.push(i)
        }
    }
    return answer.length===0?[-1]:answer;
}