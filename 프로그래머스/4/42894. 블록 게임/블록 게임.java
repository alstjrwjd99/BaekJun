import java.util.*;

class Solution {

    public class Block {
        int sx, ex, sy, ey;

        public Block (int sx, int ex, int sy, int ey) {
            this.sx = sx;
            this.ex = ex;
            this.sy = sy;
            this.ey = ey;
        }
    }

    public int N;

    public int solution(int[][] board) {
        //초기화
        N = board.length;
        Block[] blocks;

        //blocks 초기화
        int blockCnt = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++)
                blockCnt = Math.max(blockCnt, board[i][j]);
        }
        blocks = new Block[blockCnt + 1];
        for (int i = 0; i < blockCnt + 1; i++)
            blocks[i] = new Block(50, -1, 50, -1);
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                int cur = board[i][j];
                if (cur == 0) continue;
                blocks[cur].sx = Math.min(blocks[cur].sx, i);
                blocks[cur].ex = Math.max(blocks[cur].ex, i);
                blocks[cur].sy = Math.min(blocks[cur].sy, j);
                blocks[cur].ey = Math.max(blocks[cur].ey, j);
            }
        }

        //시뮬레이션 시작
        //상단 경계 초기화
        int[] bounds = new int[N];
        Arrays.fill(bounds, -1);
        for (int j = 0; j < N; j++) {
            for (int i = 0; i < N; i++) {
                if (board[i][j] == 0) continue;
                bounds[j] = i;
                break;
            }
            if (bounds[j] == -1)
                bounds[j] = N;
        }

        int result = 0;
        while(true) {
            boolean breakFlag = false;  //부신 벽돌이 있으면 true;

            for (int ind = 0; ind < N; ind++) {
                //부실 수 있는지 판별할 블록
                if (bounds[ind] == N) continue;
                int cur = board[bounds[ind]][ind];

                boolean endFlag = false;
                for (int i = blocks[cur].sx; i <= blocks[cur].ex; i++) {
                    for (int j = blocks[cur].sy; j <= blocks[cur].ey; j++) {
                        //1. 현재 번호의 블록일 경우
                        if (board[i][j] == cur) continue;
                        //2. 빈 칸이며 흑돌이 들어올 수 있는 경우
                        if (board[i][j] == 0 && bounds[j] > i) continue;
                        //3. 이 외의 경우 흑돌을 체울 수 없는 경우
                        endFlag = true;
                        break;
                    }
                    if (endFlag) break;
                }
                if (endFlag) continue;

                //블록을 없앨 수 있는 경우
                result++;
                breakFlag = true;

                //1. 블록 모두 없애주기
                for (int i = blocks[cur].sx; i <= blocks[cur].ex; i++) {
                    for (int j = blocks[cur].sy; j <= blocks[cur].ey; j++) {
                        if (board[i][j] == cur)
                            board[i][j] = 0;
                    }
                }
                //2. 경계 내려주기
                for (int j = blocks[cur].sy; j <= blocks[cur].ey; j++) {
                    bounds[j] = -1;
                    for (int i = 0; i < N; i++) {
                        if (board[i][j] == 0) continue;
                        bounds[j] = i;
                        break;
                    }
                    if (bounds[j] == -1)
                        bounds[j] = N;
                }
            }

            if (!breakFlag) break;
        }
        return result;
    }
}