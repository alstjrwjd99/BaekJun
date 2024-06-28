const fs = require('fs');
let [n, arr, x] = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
arr = arr.split(' ').map(Number);
x = Number(x);
arr.sort((a, b) => a - b);

let [left, right] = [0, n - 1];
let answer = 0;

while (left < right) {
    let sum = arr[left] + arr[right];
    if (sum < x) {
        left++;
    } else if (sum > x) {
        right--;
    } else {
        answer++;
        left++;
        right--;
    }
}

console.log(answer);