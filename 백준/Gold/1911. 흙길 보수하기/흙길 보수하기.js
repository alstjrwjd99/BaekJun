const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const log = console.log;

const solution = (input) => {
  const [N, L] = input[0].split(' ').map(Number);
  const array = input.slice(1).map(v => v.split(' ').map(Number));
  const [START, END] = [0, 1];
  array.sort((a, b) => a[START] - b[START]);

  let position = 0, answer = 0;
  for (const [start, end] of array) {
    if (end <= position) continue;
    const maxStartPoint = Math.max(position, start);
    const count = Math.ceil((end - maxStartPoint) / L);
    answer += count;
    position = maxStartPoint + (count * L);
  }
  log(answer);
};

solution(input);