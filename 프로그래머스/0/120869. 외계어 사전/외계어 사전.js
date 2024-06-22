function solution(spell, dic) {
    var answer = 0;
    var tmp = 0;

    for(let i=0; i<dic.length; i++){

        for(let j=0; j<spell.length; j++){
            if(dic[i].indexOf(spell[j]) == -1){
                tmp++;
            } 
        }
        tmp > 0 ? answer = 2 : answer = 1; 
        tmp = 0;
        if(answer == 1) break;
    }

    return answer;
}