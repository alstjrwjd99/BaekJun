function solution(n, times) {
    let left = 1;
    let right = Math.max(...times) * n;
    
    const howManyClear = (elapsed) => {
        return times.reduce((acc, time) => acc + Math.floor(elapsed / time), 0);
    }
    
    while (left < right) {
        const mid = left + Math.floor((right-left)/2);
        if (howManyClear(mid) >= n) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    
    return left;
}