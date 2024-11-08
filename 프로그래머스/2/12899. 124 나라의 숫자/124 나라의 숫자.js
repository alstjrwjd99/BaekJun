function solution(n) {
    var answer = '';
    while (n > 0){
        let mod = n % 3 
        if (mod === 0){
           mod = 4
            n --
        }
        answer += mod
        n = Math.floor(n / 3)
    }
    return answer.split('').reverse().join('');
}