function solution(n) {
    const oneCnt = n.toString(2).split('').filter(a => a ==='1').length
    while (true) {
        n ++;
        if (oneCnt === n.toString(2).split('').filter(a => a ==='1').length){
            return n
        }
    }
}