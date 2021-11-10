// To try it: javac PalindromePermutation.java ; java PalindromePermutation "testcase" 
// Assumes non-letter chars should be ignored.
//
// Var single refers to the single char that gets left out if we manually cross each pair of repeated letters: 
// [t,a,c,t,c,o,a] => [t/,a,c,t/,c,o,a] => [a/,c,c,o,a/] => [c/,c/,o] => [o]. It's max value is LIM.
// The hash-like array of booleans helps keep track of letters we've seen. First time we see 'a' B[0]++, second time reset to 0. 
// String s is the clean string we can work with after removing all the crap and turning all letters to lowercase (A -> a). 
// (Java strings are immutable). 
// We only need to scan s once. Method s.length() simply returns internal count of string so no need to assign it to another var. 
// Var val is the current letter, by - 'a' we make a=0 and z=LIM-1. 
// If we've seen val before, reset to 0 (false) and reduce single (pair found). 
// Otherwise increment val (true) and increment single as this is either the first time we see val or a pair had already canceled itself out. 
// It does not matter whether s is odd or even. If single is 0 or 1, s is a palindrome. 
// If single is > 1 that means we saw a bunch of single letters. 

class PalindromePermutation {
	static boolean isPP(String str) {
		byte LIM = 26; // Assume only a-z valid. 
		byte single = 0;
		boolean[] B = new boolean[LIM];
		String s = ( (str.toLowerCase()).replaceAll("[^a-z]", "") );

		byte val;
		for (short q = 0; q < s.length(); q++) {
			val = (byte) (s.charAt(q) - 'a');
			if (B[val]) single--;
			else single++;
			B[val] = !(B[val]);
		}
		return (! (single > 1) ); 
	}

	public static void main(String Args[]) {
		System.out.println("isPP: " + Args[0] + " ==> " + isPP(Args[0]) );
	}
}

