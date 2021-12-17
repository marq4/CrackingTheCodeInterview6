
class SinglyLinkedList {
	Node Head;

	SinglyLinkedList() {
		this.Head = null; 
	}

	SinglyLinkedList(int firstData) {
		this.Head = new Node(firstData); 
	}

	boolean isEmpty() {
		return (this.Head == null); 
	}

	void add(int lastData) {
		if ( this.isEmpty() ) 
			this.Head = new Node(lastData); 
		else {
			Node Trav = this.Head; 
			while (Trav.Next != null) 
				Trav = Trav.Next; 
			Trav.Next = new Node(lastData);
		}
	}


	class Node {
		Node Next; 
		int data;  

		private Node(int newData) {
			this.Next = null; 
			this.data = newData; 
		}

		@Override 
		public String toString() {
			return "[SLLNode]: ?->(" + String.valueOf(this.data) + ")->?"; 
		}
	}

	@Override 
	public String toString() {
		String Repr = "{Singly Linked List (int) => "; 
		for (Node Trav = Head; Trav != null; Trav = Trav.Next) 
			Repr += "(" + String.valueOf(Trav.data) + ")->"; 
		return Repr + "|| } "; 
	}

}

