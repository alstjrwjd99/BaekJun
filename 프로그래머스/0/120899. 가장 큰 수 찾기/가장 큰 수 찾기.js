function solution(array) {
    var answer = [0, 0]; 
    array.forEach((num, idx) => {
        if (num > answer[0]) { 
            answer[0] = num;  
            answer[1] = idx;  
        }
    });
    return answer;
}