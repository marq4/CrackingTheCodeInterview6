/*
 * Run with -ea 
 * As the book suggests we should see a matrix as 2 rows and 2 columns 
 *   with something inside; either a dot, a single element, or a smaller matrix. 
 * Let's begin with the base scenario, n=2: 
 * M = 	[1, 2]
 * 	[3, 4] 	
 * Let's assign names to each row pointer and column pointer. Top = 1, Right = 2, Left = 3, Bottom = 4. 
 * M = 	[T, R] 
 * 	[L, B]
 * To rotate: 
 *   save Top, move Left to Top, Bottom to Left, Right to Bottom, and finally load memory into Right. 
 * M = 	[3, 1] 
 * 	[4, 2] 
 * 			(memory = 1)  
 * If the matrix is bigger than 2, we need to iterate those pointers through the rest of the row/col: 
 *   Top moves to the right (within first row). 
 *   Right moves down (within last col). 
 *   Bottom moves to the left (within last row). 
 *   Left moves up (within first col). 
 *
 * We go from the outsise "shell" and go deeper while the inner matrix is greater than a single element. 
 * Var l refers to the current depth level. Var tmp to the memory. Var rev is reverse, to go up or left. 
 * The inner for rotates shell rows and cols using l as offset. 
 * Then we reduce n as we have rotated one dimension, and increase l because we're one lever deeper. 
 */

class MatrixRotation {
	static void rotate(int[][] M) {
		assert M != null && M.length > 0 && M[0] != null && M.length == M[0].length; 

		int tmp, q, rev, l; 
		int n = M.length; 

		for (l = 0; n > 1; n--, l++) {
			for (q = l, rev = n-1; q < n-1; q++, rev--) {
				tmp = M[l][q]; 				//save tmp<-top 
				M[l][q] = M[rev][l]; 			//top<-left 
				M[rev][l] = M[n-1][rev]; 		//left<-bottom 
				M[n-1][rev] = M[q][n-1]; 		//bottom<-right 
				M[q][n-1] = tmp; 			//load right<-tmp 
			}
		}
	}


        static void showMatrix(int[][] S) {
                int f, g, a, z;
                z = S.length;
                a = 0;
                for (f = 0; f < z; f++, System.out.println()) {
                        for (g = 0; g < z; g++) {
                                if (++a > 9)
                                        System.out.print( S[f][g] + "     " );
                                else
                                	System.out.print( S[f][g] + "      " );
                        }
                }

        }

        static void fillMatrix(int[][] F) {
                int f, g, a = 0;
                int x = F.length;
                for (f = 0; f < x; f++)
                        for (g = 0; g < x; g++)
                                F[f][g] = ++a;
        }

        public static void main(String[] Args) {
                assert Args.length > 0;
                int x = Integer.parseInt( Args[0] );
                assert x > 0;
                int[][] TestCase = new int[x][x];
                fillMatrix(TestCase);
                System.out.println("Matrix => ");
                showMatrix(TestCase);
                rotate(TestCase);
                System.out.println("Rotated 90° => ");
                showMatrix(TestCase);
        }
}

