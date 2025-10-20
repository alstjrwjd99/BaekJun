import java.util.*;

class Solution {
    static final int INF = 1000000000;
    static final int NEG_INF = -1000000000;

    static int getOneBitCnt(int mask) {
        int cnt = 0;
        while (mask > 0) {
            cnt += (mask & 1);
            mask >>= 1;
        }
        return cnt;
    }

    public int solution(int[][] visible, int[][] hidden, int k) {
        int nRows = visible.length;
        if (nRows == 0) return 0;
        int nCols = visible[0].length;

        int initSum = 0;
        for (int[] row : visible)
            for (int val : row)
                initSum += val;

        int[][] diff = new int[nRows][nCols];
        for (int i = 0; i < nRows; i++)
            for (int j = 0; j < nCols; j++)
                diff[i][j] = hidden[i][j] - visible[i][j];

        boolean canVisitAllCells = false;
        if (nRows >= 2 && nCols >= 2)
            if (((nRows + nCols) % 2 == 0) && ((nRows * nCols) % 2 == 0))
                canVisitAllCells = true;

        int answer = NEG_INF;

        for (int rowMask = 0; rowMask < (1 << nRows); rowMask++) {
            int flipCount = getOneBitCnt(rowMask);
            int rowCost = flipCount * k;
            int baseScore = initSum - rowCost;

            int[] colFlippedSum = new int[nCols];
            int[] colNotFlippedSum = new int[nCols];

            for (int col = 0; col < nCols; col++) {
                int sumFlipped = 0, sumNotFlipped = 0;
                for (int row = 0; row < nRows; row++) {
                    if (((rowMask >> row) & 1) == 1)
                        sumFlipped += diff[row][col];
                    else
                        sumNotFlipped += diff[row][col];
                }
                colFlippedSum[col] = sumFlipped;
                colNotFlippedSum[col] = sumNotFlipped;
            }

            if (!canVisitAllCells) {
                int colTotalScore = 0;
                for (int col = 0; col < nCols; col++)
                    colTotalScore += Math.max(colFlippedSum[col], colNotFlippedSum[col] - k);
                answer = Math.max(answer, baseScore + colTotalScore);
            } else {
                int[] minOddScoreColNotFlipped = new int[nCols];
                int[] minOddScoreColFlipped = new int[nCols];
                for (int i = 0; i < nCols; i++) {
                    minOddScoreColNotFlipped[i] = INF;
                    minOddScoreColFlipped[i] = INF;
                }

                for (int col = 0; col < nCols; col++) {
                    for (int row = 0; row < nRows; row++) {
                        if (((row + col) & 1) == 1) {
                            int oddScoreColNotFlipped, oddScoreColFlipped;
                            if (((rowMask >> row) & 1) == 1) {
                                oddScoreColNotFlipped = visible[row][col] + diff[row][col];
                                oddScoreColFlipped = visible[row][col];
                            } else {
                                oddScoreColNotFlipped = visible[row][col];
                                oddScoreColFlipped = visible[row][col] + diff[row][col];
                            }
                            if (oddScoreColNotFlipped < minOddScoreColNotFlipped[col])
                                minOddScoreColNotFlipped[col] = oddScoreColNotFlipped;
                            if (oddScoreColFlipped < minOddScoreColFlipped[col])
                                minOddScoreColFlipped[col] = oddScoreColFlipped;
                        }
                    }
                }

                TreeSet<Integer> thresholdsSet = new TreeSet<>();
                for (int val : minOddScoreColNotFlipped) thresholdsSet.add(val);
                for (int val : minOddScoreColFlipped) thresholdsSet.add(val);
                Integer[] thresholds = thresholdsSet.toArray(new Integer[0]);

                int bestScore = NEG_INF;

                for (int threshold : thresholds) {
                    boolean valid = true;
                    int profitSum = 0;
                    int globalOddMin = INF;

                    for (int col = 0; col < nCols; col++) {
                        int bestColProfit = NEG_INF;
                        int chosenOdd = INF;

                        if (minOddScoreColNotFlipped[col] >= threshold) {
                            bestColProfit = colFlippedSum[col];
                            chosenOdd = minOddScoreColNotFlipped[col];
                        }

                        if (minOddScoreColFlipped[col] >= threshold) {
                            int profitOpt = colNotFlippedSum[col] - k;
                            if (profitOpt > bestColProfit) {
                                bestColProfit = profitOpt;
                                chosenOdd = minOddScoreColFlipped[col];
                            }
                        }

                        if (bestColProfit == NEG_INF) {
                            valid = false;
                            break;
                        }

                        profitSum += bestColProfit;
                        if (chosenOdd < globalOddMin)
                            globalOddMin = chosenOdd;
                    }

                    if (valid)
                        bestScore = Math.max(bestScore, baseScore + profitSum - globalOddMin);
                }

                answer = Math.max(answer, bestScore);
            }
        }

        return answer;
    }
}