/*
 * First we get rid of any crap just in case. 
 * If the two strings are the same, they are zero away so return true. 
 * If the length of the strings differs by more than 1, they can't be one away so return false. 
 * Create a Hits table to keep track of how many of each character we've seen. 
 * For each char in the first string, increment its count in H. 
 * For each char in the second string, decrement its count in H so that same chars cancel out. 
 * Now add up (var sum) absolute values of H so sum: 
 *   "aa" "ab" -> first a's cancel, 2 hits remain => 1 + |-1| = 2. (Replace) 
 *   "aaa" "aa" = 1. (Delete/Add). 
 *   "pale" "bake" -> a's & e's cancel = 4. 
 * If sum is 1 then it is one away so return true. 
 * If sum is 2 and the strings are the same length it is one away so return true. 
 * Otherwise return false. 
 */

import java.lang.Math;

class OneAway {
        static boolean oneAway(String first, String second) {
                String f = ( first.toLowerCase().replaceAll("[^a-z]", "") );
                String s = ( second.toLowerCase().replaceAll("[^a-z]", "") );

                if ( f.equals(s) ) return true;

                int dif = ( f.length() - s.length() );
                if (Math.abs(dif) > 1) return false;

                int[] H = new int[26];
                int sum = 0;
                int q;

                for (q = 0; q < f.length(); q++)
                        H[ (f.charAt(q) - 'a') ]++;

                for (q = 0; q < s.length(); q++)
                        H[ (s.charAt(q) - 'a') ]--;

                for (int h : H)
                        sum += Math.abs(h);

                if ( (sum == 2 && dif == 0) || sum == 1) return true;

                return false;
        }

        public static void main(String Args[]) {
                System.out.println("oneAway?   " + oneAway(Args[0], Args[1]) );
        }
}


