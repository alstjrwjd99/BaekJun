const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split(' ')
const start = Number(input[0])
const end = Number(input[1])

queue = [[start,0]]
visited = new Set()

answer = -1

while (queue.length !== 0){
    const [num,cnt] = queue.shift()
    const double = num*2
    const afterOne = Number(String(num)+'1')
    if(double<end && !visited.has(double) ){queue.push([double,cnt+1])}
    if(afterOne<end && !visited.has(afterOne)){queue.push([afterOne,cnt+1])}
    
    if(double === end || afterOne === end ){
        answer = cnt+2
        break
    }
}
console.log(answer)