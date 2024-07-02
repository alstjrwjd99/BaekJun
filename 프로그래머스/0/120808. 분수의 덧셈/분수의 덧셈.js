function solution(numer1, denom1, numer2, denom2) {
    numer1 *= denom2
    numer2 *= denom1
    var [n,d] = [numer1+numer2,denom1 * denom2]
    let i = 2
    let tmp = []
    while (i<=Math.min(n,d)){
        if ((n%i===0) && (d%i===0)){
            tmp.push(i)
        }
        i++
    }
    var div = tmp[tmp.length-1]
    return tmp.length===0?[n,d]:[n/div,d/div];
}