function solution(num_list) {
    return num_list.length > 10? num_list.reduce((sum,n) => sum + n,0): num_list.reduce((sum,n) => sum * n,1)
}