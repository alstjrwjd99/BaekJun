const fs = require('fs');
const n = Number(fs.readFileSync('/dev/stdin').toString().trim())

let dp = Array.from(Array(n).fill(0))

if (n == 1) console.log(1)
else if (n == 2) console.log(1)
else {
    dp[1] = 1
    dp[2] = 1
    for (let i = 2; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2]
    }
    console.log(dp[n])
}
