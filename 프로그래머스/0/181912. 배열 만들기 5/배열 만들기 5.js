function solution(intStrs, k, s, l) {
    var answer = [];
    intStrs.forEach(x => {
        var num = parseInt(x.slice(s,s+l))
        if(num > k){
            answer.push(num)
        }
    })
    return answer;
}