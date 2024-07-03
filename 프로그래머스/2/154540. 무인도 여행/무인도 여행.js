function solution(maps) {
    var answer = [];
    var visited = new Set();
    var dx = [-1, 1, 0, 0];
    var dy = [0, 0, 1, -1];

    const bfs = (x, y) => {
        var queue = [];
        queue.push([x, y]);
        visited.add(`${x},${y}`);
        var sum = parseInt(maps[x][y], 10);

        while (queue.length !== 0) {
            let [a, b] = queue.shift();
            for (let k = 0; k < 4; k++) {
                let nx = a + dx[k];
                let ny = b + dy[k];
                if (0 <= nx && nx < maps.length && 0 <= ny && ny < maps[0].length && !visited.has(`${nx},${ny}`) && maps[nx][ny] !== 'X') {
                    sum += parseInt(maps[nx][ny], 10);
                    queue.push([nx, ny]);
                    visited.add(`${nx},${ny}`);
                }
            }
        }
        return sum;
    };

    for (let i = 0; i < maps.length; i++) {
        for (let j = 0; j < maps[0].length; j++) {
            if (maps[i][j] !== 'X' && !visited.has(`${i},${j}`)) {
                answer.push(bfs(i, j));
            }
        }
    }

    answer = answer.sort((a, b) => a - b);
    return answer.length === 0 ? [-1] : answer;
}