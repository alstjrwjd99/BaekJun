function solution(before, after) {
    before = before.split('').sort().join('')
    after = after.split('').sort().join('')
    return before === after? 1:0;
}