function solution(myString) {
    var answer = myString.split('x').filter(substring => substring !== '').sort();
    return answer;
}