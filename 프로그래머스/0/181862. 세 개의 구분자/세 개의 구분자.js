function solution(myStr) {
    for(s of ['a','b','c']){
        myStr = String(myStr.split(s))
    }
    var answer = myStr.split(',').filter(x=>x!='')
    return answer.length?answer:['EMPTY'];
}