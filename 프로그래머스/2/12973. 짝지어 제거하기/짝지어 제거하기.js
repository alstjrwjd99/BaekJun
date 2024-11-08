function solution(s) {
    const stack = [];
    
    for (let char of s) {
        if (stack[stack.length - 1] === char) {
            stack.pop();  // 이전 문자가 현재 문자와 같다면 제거
        } else {
            stack.push(char);  // 다르다면 스택에 추가
        }
    }
    
    return stack.length === 0 ? 1 : 0;  // 스택이 비어있으면 1, 그렇지 않으면 0
}