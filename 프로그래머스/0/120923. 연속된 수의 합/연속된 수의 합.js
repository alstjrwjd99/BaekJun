function solution(num, total) {
    var start = Math.floor((total - Math.floor((num-1)*(num)/2))/num)
    var answer = [];
    for(let i=0;i<num;i++){
        answer.push(start+i)
    }
    return answer;
}