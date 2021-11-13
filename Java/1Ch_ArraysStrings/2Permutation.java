/*
 * To try it out: javac 2Permutation.java ; java Permutation "yyy" "yyy" 
 * Assumes any printable characters other than space are valid. 
 *
 * Instead of thinking of chars we can imagine we're comparing the digits of 2 numbers: 
 *   "abc" "cba" -> [0,1,2] [2,1,0]. 
 * We could get a "digest" of each big number by adding together all its digits, 
 *   then do the same for the other and finally substract the results: res1 - res2. 
 *   If that is 0 then both numbers must have been composed of the same digts. 
 * Instead we can also substract each pair of digits at the same position in each big number and add all up: 
 *   (0 - 2) + (1 - 1) + (2 - 0) = 0. 
 *   "da...e" "da...f" => (3 - 3) + (0 - 0) + ... + (4 - 5) = -1. 
*/

class Permutation {
	static boolean isPermutation(String First, String Second) {
                String F = First.replaceAll("\\s", "");
                String S = Second.replaceAll("\\s", "");

		if (F.length() != S.length() ) return false; 

		int sum = 0;
		for (int q = 0; q < F.length(); q++) 
			sum += ( F.charAt(q) - S.charAt(q) ); 

		return (sum == 0); 
	}

	public static void main(String Args[]) {
		System.out.println("Is permutation?   " + Args[0] + "   " + Args[1] + "   =>" + isPermutation(Args[0], Args[1]) ); 
	}
}

