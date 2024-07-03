const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const log = console.log;
let answer = 0
const solution = (input) => {
const N = Number(input[0]);
const real = Array.from({ length: N }, (_, i) => i + 1);
const array = input.slice(1)
array.sort((a, b) => a - b);
for(let i=0;i<N;i++){
    answer += Math.abs(real[i] - array[i])
}
log(answer);
};

solution(input);