function solution(my_string) {
    var answer = '';
    my_string.split('').forEach(x => {
        if(!answer.includes(x)){
            answer += x
        }
    })
    return answer;
}