function solution(n) {
    var curse = 1;
    
    const next_num = (curse) =>{
        let flag = true;
        while (flag){
            if (String(curse).includes(3) || curse % 3===0){
                curse++;
            }else{
                flag = false;
            }
        }
        return curse;
    }
    
    while (n!==1){
        curse++;
        curse = next_num(curse);
        console.log(curse)
        n--;
    }    
    return curse;
}