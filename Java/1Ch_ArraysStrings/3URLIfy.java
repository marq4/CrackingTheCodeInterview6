/*
 * Run with -ea when testing different cases to avoid weird errors in case of wrong input. 
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
                private String Str;
                private int size;
                TestCase() {
                        this.setStr("");
                        this.setSize(0);
                }
                TestCase(String NewStr, int newSize) {
                        this.setStr(NewStr);
                        this.setSize(newSize);
                }
                TestCase(String realStr, String SizeStr) {
			this(realStr, Integer.parseInt(SizeStr) );
                }
                void setStr(String S) {
                        this.Str = S;
                }
                String getStr() {
                        return this.Str;
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

	private static boolean inputValid(String Text, String RealSize) {
		if (Text == null || RealSize == null) return false; 
		int size = Integer.parseInt(RealSize); 
		if (size < 0) return false; 
		int innerSpaces = 0, trailingSpaces = 0, nonSpaceChars = 0; 
		// Count non-spaces and inner spaces:  
		for (int q = 0; q < size; q++) {
			if (Text.charAt(q) == ' ') innerSpaces++; 
			else nonSpaceChars++; 
		}
		assert (size == nonSpaceChars + innerSpaces); // Should always be true. 
		// Only trailing spaces should follow: 
		for (int q = innerSpaces + nonSpaceChars; q < Text.length(); q++) {
			if (Text.charAt(q) != ' ') return false; 
			else trailingSpaces++; 
		}
		// Now the real tests, make sure the specified size is correct and enough trailing spaces were given: 
		if (Text.length() != nonSpaceChars + innerSpaces + trailingSpaces) return false; 
		if (innerSpaces * 2 != trailingSpaces) return false;
		return true; 
	}

        public static void main(String Args[]) {
		if (Args == null || Args.length != 2) return; 
		assert inputValid(Args[0], Args[1]): 
			"Please verify that number ('true' length of string). Also the trailing spaces must be exact. "; 
                TestCase Tc = new TestCase(Args[0], Args[1]);
                System.out.println(Tc);
                char[] ReplaceMe = Tc.getStrAsCharArray();
                System.out.println("Before: " + Arrays.toString(ReplaceMe) );
                urlIfy(ReplaceMe, Tc.getSize());
                System.out.println("After:  " + Arrays.toString(ReplaceMe) );
		// Verify no spaces left: 
		for (int q = 0; q < ReplaceMe.length; q++) assert ReplaceMe[q] != ' ' : "A space remains!";  
        }
}

