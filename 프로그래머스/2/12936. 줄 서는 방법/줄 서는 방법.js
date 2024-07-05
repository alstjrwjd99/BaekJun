function solution(n, k) {
    const answer = [];
    const people = Array.from({ length: n }, (_, i) => i + 1);
    let fac = people.reduce((ac, v) => ac * v, 1)
    
    while (answer.length < n) {
        fac /= people.length;
        answer.push(...people.splice(Math.floor((k - 1) / fac), 1));
        k %= fac;
    }

    return answer;
}