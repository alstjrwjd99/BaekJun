function solution(n) {
    var answer = 1;
    while ((answer * 6)%n!==0 ){
        answer += 1
    }
    return answer;
}