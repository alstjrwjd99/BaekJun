function solution(n, slicer, num_list) {
    var [a,b,c] = [slicer[0],slicer[1],slicer[2]]
    if(n===1){return num_list.slice(0,b+1)}
    else if(n===2){return num_list.slice(a)}
    else if(n===3){return num_list.slice(a,b+1)}
    else if(n===4){return num_list.filter((_,idx)=>idx>=a && idx<=b && (idx+a)%c==0)}
}