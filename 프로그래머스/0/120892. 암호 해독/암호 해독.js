function solution(cipher, code) {
    var answer = '';
    answer = cipher.split('').filter((s,index)=> (index+1) %code==0 ).join('')
    return answer;
}