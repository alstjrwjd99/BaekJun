function solution(numbers) {
    var answer = numbers.reduce((num,sum_val) => sum_val + num, 0) / numbers.length;
    return answer;
}