function solution(arr) {
    var answer = [];
    arr.forEach((n)=>{
        answer.push(...Array(n).fill(n))
    })
    return answer;
}