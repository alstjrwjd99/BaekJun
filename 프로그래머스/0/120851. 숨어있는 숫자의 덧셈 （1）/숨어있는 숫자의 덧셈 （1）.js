function solution(my_string) {
    var answer = my_string.split('')
        .filter(s => !isNaN(s) && s !== '')
        .reduce((sum,i) => sum + Number(i) , 0)
    return answer;
}