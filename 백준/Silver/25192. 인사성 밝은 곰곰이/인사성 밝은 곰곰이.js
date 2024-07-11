const fs = require('fs')
let [n,...input] = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
n = Number(n)
let answer = 0
let member = new Set()

for(let name of input){
    if(name==='ENTER'){
        answer += member.size
        member.clear()
    }else{
        member.add(name)
    }
}
console.log(answer+member.size)