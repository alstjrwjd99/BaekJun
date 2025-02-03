function solution(elements) {
    var answer = new Set();
    const double = [...elements, ...elements]
    const slidingWindow = (len) => {
        for (let i = 0; i< elements.length; i ++){
            answer.add(double.slice(i,i+len).reduce((acc,cur) => acc +cur, 0))
        }
    }
    
    for (let i = 1; i <= elements.length ; i ++){
        slidingWindow(i)
    }
    return answer.size;
}