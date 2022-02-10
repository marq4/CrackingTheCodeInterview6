
import java.util.Queue; 
import java.util.ArrayList; 
import java.util.ArrayDeque; 

final class RouteBetweenNodes {
	private static final byte VERTICES = (byte) 10; 

	private static final AdjacencyMatrixGraph createExampleGraph() {
		assert VERTICES > 0; 
		AdjacencyMatrixGraph Example = new AdjacencyMatrixGraph(VERTICES); 
		Example.addEdge( (byte) 0,  (byte) 1, false); 
		Example.addEdge( (byte) 0,  (byte) 2, false); 
		Example.addEdge( (byte) 0,  (byte) 3, false); 
		Example.addEdge( (byte) 1,  (byte) 2, false); 
		Example.addEdge( (byte) 1,  (byte) 5, false); 
		Example.addEdge( (byte) 1,  (byte) 4, false); 
		Example.addEdge( (byte) 2,  (byte) 5, false); 
		Example.addEdge( (byte) 2,  (byte) 6, false); 
		Example.addEdge( (byte) 5,  (byte) 8, false); 
		Example.addEdge( (byte) 8,  (byte) 6, false); 
		Example.addEdge( (byte) 3,  (byte) 7, false); 
		Example.addEdge( (byte) 7,  (byte) 9, false); 
		Example.addEdge( (byte) 4,  (byte) 5, false); 
		return Example; 
	}

	/* 
	 * Returns true if src and dst vertices are connected in 
	 * Adjacency Matrix Graph. (Ignores self-loops.) 
	 * If any arguments are invalid returns false. 
	 * A vertex is connected to itself. 
	 * Visited keeps track of seen vertices, 
	 * 	false: unvisited, true: visiting/visited. 
	 * VisitLater should be used as a Queue. (Java Queue is abstract.) 
	 * First mark src as visited and add its adjacent vertices 
	 * 	to the Queue for visiting later. 
	 * Neighbours is a pointer to dynamic array. 
	 * While there's nodes in the Queue, 
	 * 	Get the next neighbours to visit. 
	 * 	For each neighbour, if it hasn't been visited, 
	 * 		If that is the destination return true. 
	 * 		Otherwise mark it as visited and add its 
	 * 			adjacent vertices to the Queue. 
	 * Return false if path not found. 
	 */
	public static boolean BFSM(AdjacencyMatrixGraph Graph, byte src, byte dst) {
		if (Graph == null) return false;  
		if (src < 0 || dst < 0) return false; 
		byte numNodes = Graph.getNumVertices(); 
		if (numNodes < 1 || src >= numNodes || dst >= numNodes) return false; 

		if (src == dst) return true; 

		boolean[] Visited = new boolean[numNodes]; 

		final Queue< ArrayList<Byte> > VisitLaterQ = new ArrayDeque< ArrayList<Byte> >(); 

		Visited[src] = true; 
		VisitLaterQ.add( Graph.getAdjacentNodes(src) ); 

		ArrayList<Byte> Neighbours; 
		while ( !( VisitLaterQ.isEmpty() ) ) {
			Neighbours = VisitLaterQ.remove(); 
			if (Neighbours == null) continue; 
			for (byte n : Neighbours) {
				if (Visited[n]) continue; 
				if (n == dst) return true; 
				Visited[n] = true; 
				VisitLaterQ.add( Graph.getAdjacentNodes(n) );
			}
		}

		return false; 
	}

	private static final void showASCIIGraph() {
		String Repr = 	"    -> 3 -> 7 -> 9.\n" + 
				"   /\n" + 
				"  0-->  2  ----> 6 <\n" + 
				"  \\     ^\\____   V    \\\n" + 
				"   \\   /      \\> }     \\\n" +
				"    > 1 -> 4 --> } 5 -> 8\n" + 
				"      \\________> }\n"; 
		System.out.println(Repr); 
	}

	public static void main(String[] Args) {
		if (Args == null || Args.length != 2) return; 
		AdjacencyMatrixGraph MyGraph = createExampleGraph(); 
		//System.out.println(MyGraph); 
		showASCIIGraph(); 
		System.out.println("Are connected? " + Args[0] + ", " + Args[1]); 
		System.out.print( String.valueOf( BFSM( MyGraph, 
			Byte.parseByte( Args[0]), Byte.parseByte(Args[1]) ) ) ); 
	}
	/* Run: -ea RouteBetweenNodes, ^^ Args: {byte} source, {byte} destination . */

}

