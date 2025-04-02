import java.io.*;
import java.util.StringTokenizer;

public class Main {
    static int[][] arr;
    static int N,M;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());

        arr = new int[n][m];
        N = n;
        M = m;

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 0; i < r; i++) {
            rotate();
        }
        display();
    }

    static void rotate() {
        int layers = Math.min(N, M) / 2;

        for (int layer = 0; layer < layers; layer++) {
            int top = layer;
            int bottom = N - 1 - layer;
            int left = layer;
            int right = M - 1 - layer;

            int[] temp = new int[2 * (right - left + bottom - top) * 1];
            int idx = 0;

            for (int j = left; j <= right; j++) temp[idx++] = arr[top][j];
            for (int i = top + 1; i <= bottom; i++) temp[idx++] = arr[i][right];
            for (int j = right - 1; j >= left; j--) temp[idx++] = arr[bottom][j];
            for (int i = bottom - 1; i > top; i--) temp[idx++] = arr[i][left];

            int[] rotated = new int[temp.length];
            for (int i = 0; i < temp.length; i++) {
                rotated[i] = temp[(i + 1) % temp.length];
            }

            idx = 0;
            for (int j = left; j <= right; j++) arr[top][j] = rotated[idx++];
            for (int i = top + 1; i <= bottom; i++) arr[i][right] = rotated[idx++];
            for (int j = right - 1; j >= left; j--) arr[bottom][j] = rotated[idx++];
            for (int i = bottom - 1; i > top; i--) arr[i][left] = rotated[idx++];
        }


    }
    static void display(){

        for (int i = 0; i < N; i++) {
            for (int j=0;j<M;j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }

    }
}
