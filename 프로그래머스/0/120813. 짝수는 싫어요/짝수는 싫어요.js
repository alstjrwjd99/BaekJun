function solution(n) {
    var numbers = Array.from({ length: n }, (_, i) => i + 1);
    var answer = numbers.filter(num => num % 2 !== 0);
    return answer;
}