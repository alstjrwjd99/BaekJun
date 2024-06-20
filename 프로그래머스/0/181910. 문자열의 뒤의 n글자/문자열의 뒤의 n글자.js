function solution(my_string, n) {
    var answer = my_string.split('')
        .filter((_,idx)=> idx > my_string.length - n -1)
        .join('');
    return answer;
}
