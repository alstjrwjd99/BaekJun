function solution(k, d) {
    var answer = ~~(d/k) + 1;
    for(let i =0;i<d;i+=k){
        const y = (d-i) ** (1/2) * (d+i) ** (1/2)
        answer += ~~((~~y)/k)
    }
    
    return answer;
}