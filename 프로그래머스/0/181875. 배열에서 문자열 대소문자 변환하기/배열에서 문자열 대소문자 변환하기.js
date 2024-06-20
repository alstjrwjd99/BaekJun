function solution(strArr) {
    var answer =
    strArr.map((s,idx)=>{return idx%2===0?s.toLowerCase():s.toUpperCase()})
    return answer;
}