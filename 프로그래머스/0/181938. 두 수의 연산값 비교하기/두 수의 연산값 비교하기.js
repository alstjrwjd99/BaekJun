function solution(a, b) {
    var int = Number(String(a)+String(b))
    return int>=2*a*b?int:a*b*2
}