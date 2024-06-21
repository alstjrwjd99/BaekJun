function solution(my_string, indices) {
    var answer = 
    my_string.split('').filter((x,idx)=>!indices.includes(idx)).join("")
    return answer;
}