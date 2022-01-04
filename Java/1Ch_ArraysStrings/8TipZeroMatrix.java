/*
 * As book suggests we can use the top row and first col to store found 0s.
 *      BUT then we must zero them out at the end to prevent entire Matrix from becoming 0.
 * For each element (r,c) in the Matrix:
 *   if it's 0, set element's top row (0,c) and first col (r,0) to 0.
 * For each element in top row (0,c):
 *   if it's 0, overwrite entire column with 0.
 * For each element in first column (r,0):
 *   if it's 0, overwrite entire row with 0.
 */

import java.util.Arrays;

final class ZeroMatrixTip {
        static void zeroRC(int[][] Matrix) {
                if (Matrix == null || Matrix.length < 1 || Matrix[0] == null || Matrix[0].length < 1) return;

                int m = Matrix.length;
                int n = Matrix[0].length;
                if (m == 1 && n == 1) return;

                int row, col;
                for (row = 0; row < m; row++) for (col = 0; col < n; col++) assert Matrix[row] != null; //run with -ea
                boolean todo0Top = false, todo0Left = false;

                // Find 0s:
                for (row = 0; row < m; row++)
                        for (col = 0; col < n; col++)
                                if (Matrix[row][col] == 0) {
                                        if (row == 0) todo0Top = true; 
					else Matrix[0][col] = 0; 
                                        if (col == 0) todo0Left = true;
					else Matrix[row][0] = 0; 
                                }
                //  Overwrite with 0s EXCEPT TOP ROW AND FIRST COL:
                for (col = 1; col < n; col++)
                        if (Matrix[0][col] == 0)
                                for (row = 1; row < m; row++)
                                        Matrix[row][col] = 0;
                for (row = 1; row < m; row++)
                        if (Matrix[row][0] == 0)
                                for (col = 1; col < n; col++)
                                        Matrix[row][col] = 0;
                // Finally top row and first col:
                if (todo0Top) for (col = 0; col < n; col++) Matrix[0][col] = 0;
                if (todo0Left) for (row = 0; row < m; row++) Matrix[row][0] = 0;

        }

        static void showMatrix(int[][] S) {
                int f, g, a = 0;
                for (f = 0; f < S.length; f++, System.out.println()) {
                        for (g = 0; g < S[f].length; g++) {
                                if (++a > 12)
                                        System.out.print( S[f][g] + "     " );
                                else if (a > 9)
                                        System.out.print( S[f][g] + "     " );
                                else
                                System.out.print( S[f][g] + "      " );
                        }
                }

        }

        static void fillMatrix(int[][] F) {
                int f, g, a = 0;
                for (f = 0; f < F.length; f++)
                        for (g = 0; g < F[f].length; g++)
                                F[f][g] = ++a;
        }


        public static void main(String[] Args) {
                if (Args.length != 2) return;
                int m = Integer.parseInt( Args[0] );
                int n = Integer.parseInt( Args[1] );
                if (m < 1 || n < 1) return;
                int[][] TestCase = new int[m][n];
                fillMatrix(TestCase);
                int zeroRow = 0;
                int zeroCol = 0;
                assert zeroRow < m && zeroCol < n: "Matrix has to be bigger. " +
                        "Setting 0 at (" + String.valueOf(zeroRow) + ", " + String.valueOf(zeroCol) + "). ";
                TestCase[zeroRow][zeroCol] = 0;
             	//TestCase[m-1][n-1] = 0;
                System.out.println("Matrix => ");
                showMatrix(TestCase);
                zeroRC(TestCase);
                System.out.println("zeroRC => ");
                showMatrix(TestCase);
                assert TestCase[zeroRow][n-1] == 0 && TestCase[m-1][zeroCol] == 0; //run with -ea
        }
}

