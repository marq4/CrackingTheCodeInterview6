
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

		Node(int firstData) {
			this.Next = null; 
			this.data = firstData; 
		}

		public String toString() {
			return "[SLLNode] ?->(" + String.valueOf(this.data) + ")->?"; 
		}
	}

	public String toString() {
		Node Trav = Head; 
		String Repr = "SLL => "; 
		while (Trav != null) {
			Repr += "(" + String.valueOf(Trav.data) + ")->"; 
			Trav = Trav.Next; 
		}
		Repr += "|| ";
		return Repr; 
	}
}

