function solution(rank, attendance) {
    var answer = 0;
    rank = rank.map((x,idx)=>{
        if(attendance[idx]){
            return [x,idx]
        }
    }).sort((a,b)=>a[0]-b[0])
    return rank[0][1]*10000 + rank[1][1]*100 + rank[2][1];
}