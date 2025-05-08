import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int[][] board;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        board = new int[N][N];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        System.out.println(dfs(board, 0));
    }

    static int dfs(int[][] board, int cnt) {
        if (cnt == 5) {
            int max = 0;
            for (int[] row : board) {
                for (int value : row) {
                    max = Math.max(max, value);
                }
            }
            return max;
        }

        return Math.max(
            Math.max(dfs(up(copy(board)), cnt + 1), dfs(down(copy(board)), cnt + 1)),
            Math.max(dfs(left(copy(board)), cnt + 1), dfs(right(copy(board)), cnt + 1))
        );
    }

    static int[][] up(int[][] board) {
        for (int j = 0; j < N; j++) {
            int pointer = 0;
            for (int i = 1; i < N; i++) {
                if (board[i][j] != 0) {
                    int tmp = board[i][j];
                    board[i][j] = 0;

                    if (board[pointer][j] == 0) {
                        board[pointer][j] = tmp;
                    } else if (board[pointer][j] == tmp) {
                        board[pointer][j] *= 2;
                        pointer++;
                    } else {
                        pointer++;
                        board[pointer][j] = tmp;
                    }
                }
            }
        }
        return board;
    }

    static int[][] down(int[][] board) {
        for (int j = 0; j < N; j++) {
            int pointer = N - 1;
            for (int i = N - 2; i >= 0; i--) {
                if (board[i][j] != 0) {
                    int tmp = board[i][j];
                    board[i][j] = 0;

                    if (board[pointer][j] == 0) {
                        board[pointer][j] = tmp;
                    } else if (board[pointer][j] == tmp) {
                        board[pointer][j] *= 2;
                        pointer--;
                    } else {
                        pointer--;
                        board[pointer][j] = tmp;
                    }
                }
            }
        }
        return board;
    }

    static int[][] left(int[][] board) {
        for (int i = 0; i < N; i++) {
            int pointer = 0;
            for (int j = 1; j < N; j++) {
                if (board[i][j] != 0) {
                    int tmp = board[i][j];
                    board[i][j] = 0;

                    if (board[i][pointer] == 0) {
                        board[i][pointer] = tmp;
                    } else if (board[i][pointer] == tmp) {
                        board[i][pointer] *= 2;
                        pointer++;
                    } else {
                        pointer++;
                        board[i][pointer] = tmp;
                    }
                }
            }
        }
        return board;
    }

    static int[][] right(int[][] board) {
        for (int i = 0; i < N; i++) {
            int pointer = N - 1;
            for (int j = N - 2; j >= 0; j--) {
                if (board[i][j] != 0) {
                    int tmp = board[i][j];
                    board[i][j] = 0;

                    if (board[i][pointer] == 0) {
                        board[i][pointer] = tmp;
                    } else if (board[i][pointer] == tmp) {
                        board[i][pointer] *= 2;
                        pointer--;
                    } else {
                        pointer--;
                        board[i][pointer] = tmp;
                    }
                }
            }
        }
        return board;
    }

    static int[][] copy(int[][] original) {
        int[][] newBoard = new int[N][N];
        for (int i = 0; i < N; i++) {
            System.arraycopy(original[i], 0, newBoard[i], 0, N);
        }
        return newBoard;
    }
}