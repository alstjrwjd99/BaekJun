function solution(id_pw, db) {
    var answer = '';
    db.map((x) => {
        if((x[0] === id_pw[0])&&(x[1] === id_pw[1])){
            answer = 'login';
        }else if((x[0] === id_pw[0])||(x[1] === id_pw[1])){
            answer = 'wrong pw';
        }else {
            answer = 'fail'
        }
    })
    return answer;
}