function solution(s)
{
    var answer = 0;
    if (s.length < 2 || isPal(s)) return s.length
    
    const expand = (left,right) =>{
        while (left>=0 && right < s.length && s[left] === s[right]){
            left--;
            right++;
        }
        return right-left-1
    }
    
    for(let i =0;i<s.length;i++){
        answer = Math.max(answer,expand(i,i+1),expand(i,i+2))
    }
    return answer;
}

function isPal(s){
    return s===s.split("").reverse().join("")
}

