function solution(hp) {
    var answer = Math.floor(hp/5);
    hp = hp % 5
    answer += Math.floor(hp/3)
    return answer + hp % 3;
}