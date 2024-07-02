function solution(common) {
    var answer = 0;
    if (common[0]+common[2] === 2* common[1]){
        answer= common[common.length-1] + common[1] - common[0]
    }else{
        answer = common[common.length-1] * Math.floor(common[1] / common[0])
    }
    return answer;
}