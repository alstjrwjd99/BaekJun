function solution(k, ranges) {
    var answer = [];
    var ubacsu = [k];
    let n =0;
    while(k!==1){
        if(k%2===0){
            k/=2
        }else{
            k = 3*k + 1
        }
        ubacsu.push(k)
        n++
    }
    var integral = []
    for(let i = 0 ;i<n;i++){
        const sum = (ubacsu[i] + ubacsu[i+1]) / 2
        integral.push(sum)
    }
    
    ranges.forEach(range =>{
      if (range == [0,0]) {
          answer.push(integral.reduce((sum,x)=>sum+x,0))
      }else if (n+range[1] < range[0]){
          answer.push(-1)
      }else{
          let tmp = 0;
          for(let ra=range[0];ra<n+range[1];ra++){
              tmp += integral[ra]
          }
          answer.push(tmp)
      }
    })
    
    return answer;
}