function solution(s) {
    const arr = s.split(' ').map(num => Number(num))
    return `${Math.min(...arr)} ${Math.max(...arr)}`;
}