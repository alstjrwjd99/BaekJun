const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const [n, m] = input[0].split(' ').map(Number);
const stuff = input.slice(1).map((line) => line.split(' ').map(Number));

const dp = Array(m + 1).fill(0);

for (let i = 0; i < n; i++) {
    let [weight, value, count] = stuff[i];

    for (let k = 1; count > 0; k *= 2) {
        const quantity = Math.min(k, count); // 현재 배수만큼 담을 수 있는 개수
        const totalWeight = weight * quantity;
        const totalValue = value * quantity;
        
        for (let j = m; j >= totalWeight; j--) {
            dp[j] = Math.max(dp[j], dp[j - totalWeight] + totalValue);
        }
        
        count -= quantity;
    }
}

console.log(dp[m]);