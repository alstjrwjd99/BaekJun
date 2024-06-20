function solution(my_string, letter) {
    return my_string.split('').filter((s)=>s!==letter).join('');
}