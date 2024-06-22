function solution(keyinput, board) {
    var answer = [];
    const dir = {
    "left": (x, y) => ({x:x-1, y:y}), 
    "right": (x, y) => ({x:x + 1, y:y}),
    "up": (x, y) => ({x:x, y:y + 1}),
    "down": (x, y) => ({x:x, y:y - 1}) 
    };
    let len_x = (board[0]-1)/2
    let len_y = (board[1]-1)/2
    var move = {x:0,y:0}
    keyinput.forEach(key=>{
        var tmp = dir[key](move.x,move.y)
        if(tmp.x>=-len_x && tmp.x<=len_x && tmp.y>=-len_y && tmp.y<=len_y){
            move = dir[key](move.x,move.y)    
        }
        console.log(move)
    })
    return [move.x,move.y];
}