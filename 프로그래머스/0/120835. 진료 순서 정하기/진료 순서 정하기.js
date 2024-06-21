function solution(emergency) {
    var answer = [];
    var origin = emergency.slice(0)
    emergency.sort((a,b) => (b-a))
    answer = origin.map(x=>emergency.indexOf(x)+1)
    return answer;
}