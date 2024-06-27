function solution(polynomial) {
    var answer = '';
    var x = 0;
    var num = 0;
    polynomial = polynomial.split(' + ')
    polynomial.forEach(poly => {
        if(poly.includes('x')){
            poly.length===1?x+=1:x+=Number(poly.substring(0,poly.length-1))
        }
        else num+=Number(poly)
    })
    x === 1?x='':x
    return num===0?`${x}x`:x===0?`${num}`:`${x}x + ${num}`;
}