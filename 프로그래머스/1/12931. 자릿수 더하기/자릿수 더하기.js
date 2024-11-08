function solution(n) {
    var answer = n.toString().split('').reduce((acc, cur) => Number(acc) + Number(cur) , 0)
    return answer;
}