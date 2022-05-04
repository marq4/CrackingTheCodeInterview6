/*
 * Remove duplicates of an <int> Singly Linked List. 
 * Node Curr begins at the head of the list until we reach the end of the list (null). 
 * Node Runner is what we use to compare with Curr to find duplicates. 
 * Node Prev is needed to connect the first half list to the remainer of the list after 
 * 	deleting a node. 
 * While we haven't reached the end of the list: 
 * 	if we find a duplicate we need to: 
 * 		+ Connect previous to the next of the one we're about to delete. 
 * 		+ Help gc to clear memory of duplicated node. 
 * 		+ Continue cheking the rest of the list. 
 * 	otherwise just continue searching. 
 */

final class SLLRemoveDups {
	static void removeDups(SinglyLinkedList SLL) {
		SinglyLinkedList.Node Curr, Runner, Prev; 
		Curr = SLL.Head; 
		while (Curr != null) {
			Prev = Curr; 
			Runner = Curr.Next; 
			while (Runner != null) {
				if (Curr.data == Runner.data) { //delete dup: 
					Prev.Next = Runner.Next; 
					Runner = null; 
					Runner = Prev.Next; 
				} else {
					Runner = Runner.Next; 
					Prev = Prev.Next; 
				}
			}
			Curr = Curr.Next; 
		}
	}

	public static void main(String[] Args) {
		if (Args == null || Args.length < 1) return; 
		SinglyLinkedList TestCase = new SinglyLinkedList(); 
		for (int a = 0; a < Args.length; a++) TestCase.add( Integer.parseInt(Args[a]) ); 
		System.out.println("Before: " + TestCase); 
		removeDups(TestCase); 
		System.out.println("After:  " + TestCase); 
	}
	/* Run: SLLRemoveDups, ^^ Args: {int}s list of numbers to add to SLL. Expected result: removed duplicates. */

}

