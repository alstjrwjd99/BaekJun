function solution(a, b) {
    const n1 = +(a+''+b) 
    const n2 = +(b+''+a)
    return n1>=n2?n1:n2;
}