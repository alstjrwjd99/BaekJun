function solution(arr, query) {
    var answer = [];
    query.forEach((x,idx)=>{
        idx%2===0?arr=arr.slice(0,x+1):arr=arr.slice(x)
    })
    return arr;
}