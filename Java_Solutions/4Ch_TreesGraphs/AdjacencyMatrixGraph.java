
import java.lang.IllegalArgumentException; 
import java.util.ArrayList; 

public class AdjacencyMatrixGraph {
	private final static byte MAX_VERTICES = Byte.MAX_VALUE; 
	private byte numVertices; 
	private boolean[][] AdjMx; 

	public AdjacencyMatrixGraph(byte finalNumVertices) throws IllegalArgumentException {
		if (finalNumVertices < 1 || finalNumVertices > MAX_VERTICES) 
			throw new IllegalArgumentException("Number of vertices " + 
				"must be between 1 and " + 
				String.valueOf(MAX_VERTICES) ); 
		this.numVertices = finalNumVertices; 
		this.AdjMx = new boolean[numVertices][numVertices]; 
	}

	public byte getNumVertices() {
		return this.numVertices; 
	}

	/* Creates an edge between src and dst vertices, undirected. */
	public boolean connectVertices(byte src, byte dst) {
		return ( this.addEdge(src, dst, true) );
	}

	public boolean addEdge(byte src, byte dst, boolean undirected) {
		if (src < 0 || dst < 0 || src >= this.numVertices || dst >= this.numVertices) 
			return false; 
		this.AdjMx[src][dst] = true; 
		if (undirected) 
			this.AdjMx[dst][src] = true; 
		return true; 
	}

	public ArrayList<Byte> getAdjacentNodes(byte vertex) throws IllegalArgumentException {
		if (vertex < 0 || vertex > this.numVertices) 
			throw new IllegalArgumentException("Wrong vertex. "); 
		ArrayList<Byte> Adjacent = new ArrayList<Byte>(this.numVertices); 
		for (byte col = 0; col < this.numVertices; col++) 
			if (this.AdjMx[vertex][col]) 
				Adjacent.add(col); 
		return Adjacent; 
	}

	@Override 
	public String toString() {
		String Repr = "{Adjacency Matrix Graph => \n ";
		Repr += "Number of vertices: " + 
			String.valueOf(this.numVertices) + "\n"; 
		Repr += "    "; 
		for (byte header = 0; header < this.numVertices; header++) 
			Repr += String.valueOf(header) + " "; 
		Repr += "\n    "; 
		for (byte und = 0; und < this.numVertices; und++) 
			Repr += "_ "; 
		Repr += "\n"; 
		for (byte row = 0; row < this.numVertices; row++) {
			Repr += String.valueOf(row) + ") "; 
			for (byte col = 0; col < this.numVertices; col++) {
				Repr += " " + String.valueOf(
					(this.AdjMx[row][col]) ? "1" : "0" ); 
			}
			Repr += "\n"; 
		}
		return Repr += "}. "; 
	}
}

