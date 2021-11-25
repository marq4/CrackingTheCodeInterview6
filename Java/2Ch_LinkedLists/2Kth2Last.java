import java.util.HashMap; 

/*
 * Brute force: iterate twice. First time get length of list, second get kth to last node. BAD. 
 * Throw a HashMap at the problem: if we're allowed to only return the data. 
 * 	This would use a ton of extra space if the list is very long. 
 * Recursive: unnecessary nonsense (brute force is less bad. Only if forced by interviewer). BAD. 
 * Best: two pointers: runner/waiter. 
 *
 * If k is length of list -1 or greater, return head. 
 * 	EXCEPT for recursive where k has to be correct. 
 */

class SLLKth2Last {
	// If we need more than 32k calls we're doing something wrong: 
	private static short index = -1; 

	//BAD CODE: 
	static SimplyLinkedList.Node kth2LastTwice(SimplyLinkedList SLL, int k) {
		if (SLL == null) return null; 
		SimplyLinkedList.Node Trav = SLL.Head; 
		// Get list length: 
		int len; 
		for (len = 0; Trav != null; len++) Trav = Trav.Next; 
		if (k >= len) return SLL.Head; 
		// Go back to kth to last: 
		Trav = SLL.Head; 
		for (int q = 0; q < len-k-1; q++) Trav = Trav.Next; 
		return Trav; 
	}

	//Extra space: 
	static int kth2LastHash(SimplyLinkedList SLL, int k) throws IllegalArgumentException {
		if ( SLL == null || SLL.isEmpty() ) throw new IllegalArgumentException("List is empty. "); 
		SimplyLinkedList.Node Trav = SLL.Head; 
		int len; 
		HashMap<Integer, Integer> Hash = new HashMap<Integer, Integer>(); 
		for (len = 0; Trav != null; len++, Trav = Trav.Next) Hash.put(len, Trav.data); 
		if (k >= len) return SLL.Head.data; 
		return Hash.get( len-k-1 ); 
	}

	/*
	 * Make sure k is valid before calling this method. 
	 * Although this insane and absurd code works it shouldn't be used. 
	 * Base case: Head is null. We're either at the end of the list or list is empty. 
	 * Otherwise create a new pointer that will 'dive' to the rest of the list. 
	 * Var index is shared by all method calls in the stack. 
	 * When index (depth of recursion) is equal to k, return that node. 
	 * 	All calls before this return null as the end of the list bubbles up. 
	 * 	All calls after this will return the node we want all the way up to the external caller. 
	 * Example: 
	 * SLL => {10->20->30->40->||} 
	 * recurse(*10, 2): not null, 
	 * 	Diver{0} = recurse(*20, 2): not null, 
	 * 		Diver{1} = recurse(*30, 2): not null, 
	 * 			Diver{2} = recurse(*40, 2): not null, 
	 * 				Diver{3} = recurse(null, 2): return null. 
	 * 			index = 0, return null 
	 * 		index = 1, return null 
	 * 	index = 2 is equal to k, return *20 
	 * return *20. 
	 */
	//BAD CODE: 
	static SimplyLinkedList.Node kth2LastRecurs(SimplyLinkedList.Node Head, int k) {
		if (Head == null) return null; 
		SimplyLinkedList.Node Diver = kth2LastRecurs(Head.Next, k); 
		assert index > -2: "Var index has overflown. "; 
		if (++index == k) return Head; 
		return Diver; 
	}

	/*
	 * Runner goes node by node to the end of the list. 
	 * Waiter waits for it until Runner has advanced k nodes. 
	 * When Runner's next gets to null, Waiter is kth to last node. 
	 */
	//Best:
	static SimplyLinkedList.Node kth2Last2Pointers(SimplyLinkedList SLL, int k) {
		if ( SLL == null || SLL.isEmpty() ) return null; 
		SimplyLinkedList.Node Runner, Waiter; 
		int len = 0; 
		Runner = SLL.Head; Waiter = SLL.Head; 
		while (Runner.Next != null) {
			if (len++ >= k) 
				Waiter = Waiter.Next; 
			Runner = Runner.Next; 
		}
		if (k >= ++len) return SLL.Head; 
		return Waiter; 
	}

	private static boolean inputValid4Recurs(SimplyLinkedList GetMySize, int k) {
		if ( GetMySize.isEmpty() || k < 0) return false; 
		int len = 0; 
		SimplyLinkedList.Node Trav = GetMySize.Head; 
		while (Trav.Next != null) { 
			len++; 
			Trav = Trav.Next; 
		}
		return (++len > k); 
	}

	public static void main(String[] Args) {
		if (Args == null || Args.length != 1) return; 
		int kValue = Integer.parseInt(Args[0]); 
		if (kValue < 0) return; 
		SimplyLinkedList TestCase = new SimplyLinkedList(); 
		for (byte a = 10; a < 14; a++) TestCase.add(a); 
		assert !( TestCase.isEmpty() ): "SLL should not be empty. "; 
		System.out.println(TestCase); 
		int resultBF = (kth2LastTwice(TestCase, kValue)).data; 
		int resultHash = kth2LastHash(TestCase, kValue); 
		assert inputValid4Recurs(TestCase, kValue): 
			"Value k can't be greater than list length -1 for recursive method. "; 
		int resultRecurs = (kth2LastRecurs(TestCase.Head, kValue)).data; 
		int resultPointers = (kth2Last2Pointers(TestCase, kValue)).data; 
		assert resultBF == resultHash && resultBF == resultRecurs && resultBF == resultPointers; //java -ea 
		System.out.println("Value kth to last: " + String.valueOf(resultPointers) ); 
	}
}


