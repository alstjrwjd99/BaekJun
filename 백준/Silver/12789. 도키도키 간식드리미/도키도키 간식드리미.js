const fs = require('fs')
let [n,number] = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
n = Number(n)
number = number.split(' ').map((x)=>Number(x))
const YES = "Nice"
const NO = "Sad"

let stack = []
let answer = ''
let [food,i] = [1,0]

while (i<=n){
    if (number[i] === food){
        food++
        i++
    }else if(stack.length!==0 && stack[stack.length-1]===food){
        stack.pop()
        food++
    }
    else {
        stack.push(number[i])
        i++
    }
}
answer = food===n+1?YES:NO
console.log(answer)