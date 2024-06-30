function solution(code) {
    var answer = '';
    let mode = 0;
    [...code].forEach((x,idx)=> {
        if(mode === 0){
            if(x !== '1' && idx%2===0){
                answer += x
            }else if (x === '1' ) {
                mode = 1
            }
        }else if (mode === 1){
            if(x !== '1' && idx%2===1){
                answer += x
            }else if (x==='1') {
                mode = 0
            }
        }
    })
    return answer.length===0?"EMPTY":answer;
}