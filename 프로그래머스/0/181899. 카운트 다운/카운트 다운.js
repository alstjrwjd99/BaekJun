function solution(start_num, end_num) {
    var answer = Array.from(
        { length: start_num - end_num + 1 },
        (_, i) => start_num - i
    );
    return answer;
}
