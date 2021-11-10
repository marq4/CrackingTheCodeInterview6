/*
 * Input: ["Mr John Smith    ", 13]. Output: ["Mr%20John%20Smith"]. 
 * There are 2 relevant lengths: The total (var t) length of the string with all spaces, and the size (length of string with inner spaces). 
 * We can begin scanning the string from the relevant end ('h') (var q) in reverse. 
 * Whenever we see a space we replace with %20, otherwise replace with that character. 
 * We replace from the total length in reverse. 
 *               q    t              q    t                   qt                  q t                   qt
 * ["Mr John Smith    "] => ["Mr John SmitSmith"] => ["Mr John S%20Smith"] => ["Mr JoJohn%20Smith"] => ["Mr%20John%20Smith"]
 * I like to use q, w, e for iterators intead of i, j because i and j look very simmilar to ';' in paper/whiteboard. 
*/

import java.util.Arrays;

class URLIfy {
	// ' ' => '%20': 
	static void urlIfy(char[] A, int size) {
		int t = A.length-1;
                char c;
                for (int q = size-1; q > -1; q--) {
                        c = A[q];
                        if (c == ' ') {
                                A[t--] = '0';
                                A[t--] = '2';
                                A[t--] = '%';
                        } else A[t--] = c;
                }
        }

	// Java syntax showcase: 
        private static class TestCase {
                private String str;
                private int size;
                TestCase() {
                        this.setStr("");
                        this.setSize(0);
                }
                TestCase(String newStr, int newSize) {
                        this.setStr(newStr);
                        this.setSize(newSize);
                }
                TestCase(String realStr, String sizeStr) {
			this(realStr, Integer.parseInt(sizeStr) );
                }
                void setStr(String s) {
                        this.str = s;
                }
                String getStr() {
                        return this.str;
                }
                void setSize(int z) {
			if (z < 0) throw new IllegalArgumentException("Size Can't be negative");
                        this.size = z;
                }
                int getSize() {
                        return this.size;
                }
                char[] getStrAsCharArray() {
                        return this.getStr().toCharArray();
                }
                public String toString() {
                        return "TestCase: [\"" + this.getStr() + "\", " + this.getSize() + "] ";
                }
        }

        public static void main(String Args[]) {
                TestCase tc = new TestCase(Args[0], Args[1]);
                System.out.println(tc);
                char[] ReplaceMe = tc.getStrAsCharArray();
                System.out.println("Before: " + Arrays.toString(ReplaceMe) );
                urlIfy(ReplaceMe, tc.getSize());
                System.out.println("After:  " + Arrays.toString(ReplaceMe) );
        }
}

