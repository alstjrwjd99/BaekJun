function solution(arr) {
    let gcd = (a,b) => (a%b ? gcd(b, a%b) : b)
    let lcm = (a,b) => (a*b / gcd(a,b))
    return arr.reduce((acc,cur) => lcm(acc,cur) , 1);
}