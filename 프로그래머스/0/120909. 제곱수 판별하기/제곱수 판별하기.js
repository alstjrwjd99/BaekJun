function solution(n) {
    var i = 1;
    var answer = 2;
    while (i ** 2 <= n){
        i += 1
        if(i ** 2 === n){
           answer = 1 
            break
        }
    }
    return answer;
}