function solution(numbers, k) {
    var answer = 0;
    for(let i = 0 ; i<k-1;i++){
        numbers[answer%numbers.length]
        answer += 2
    }
    return numbers[answer%numbers.length];
}