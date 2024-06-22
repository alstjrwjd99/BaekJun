function solution(q, r, code) {
    var answer = code.split('').filter((x,idx)=> (idx%q) === r).join('')
    return answer;
}