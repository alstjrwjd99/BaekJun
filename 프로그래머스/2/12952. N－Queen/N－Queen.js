function solution(n) {
  let answer = 0
  
  const nQueen = (board, row) => {
    // 만약 현재 행과 n이 같다면 완성된 board를 출력해 주고 카운트++
    if(row === n) {
      answer += 1
      
    // 아니라면 탐색해야할 줄이 더 있음 
    } else {
      for (let i = 1; i <= n; i++) {
        // 다음 행에 i를 넣음 (열을 의미) <-깊이 탐색
        board[row + 1] = i
        
        // 가지치기를 하고 유망하면(?) nQueen으로 다음 행으로 재귀
        if(checker(board, row + 1)) nQueen(board, row + 1);
      }
    }
  }

  const checker = (board, row) => {
    for (let i = 1 ; i < row ; i++) {
      // board[i]는 현재행을 의미, board[row]는 다음행을 의미. 
      // 같다는 것은 현재행(기물의 위치)와 다음에 놓을 기물의 위치를 계산함. 
      // 행은 이미 조건으로 했으니, 같은 열에 있는지, 대각선으로 있는지만 검사.
      if (board[i] === board[row]) return false
      if (Math.abs(board[i] - board[row]) === Math.abs(i - row)) return false
    }
    return true
  }

  for (let i = 1; i <=n; i++) {
    // n번째 행과 index를 맞추기 위해 n + 1 만큼 생성
    let board = new Array(n + 1).fill(0)
    // 초기값: [1, 1]에 기물을 놓음
    // 1번행의 열을 반복함 1~4
    board[1] = i
    // 1차원 배열의 인덱스가 row, 값이 col을 의미함.
    // (굳이 2차원 배열을 쓰지 않아도 된다)
    // board는 케이스 보드, 이미 입력된 값이 담긴 row 행
    nQueen(board, 1)
  }
  
  return answer;
}