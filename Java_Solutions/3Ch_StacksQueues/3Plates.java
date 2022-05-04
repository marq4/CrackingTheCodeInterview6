
final class Plates {
	public static void main(String[] Args) {
		if (Args == null || Args.length != 1) return; 
		SetOfStacks TestCase = new SetOfStacks(3); 

		TestCase.push(1); 
		TestCase.push(2); 
		TestCase.push(3);
		TestCase.push(4); 
		TestCase.push(5); 
		TestCase.push(6); 
//		TestCase.push(7); 
//		TestCase.push(8); 
		System.out.println(TestCase); 

//		System.out.println("PopAt 0: " + String.valueOf( TestCase.popAt(0) ) );
//		System.out.println(TestCase); 
		System.out.println("Pop: " + String.valueOf( TestCase.pop() ) ); 
//		System.out.println("Pop: " + String.valueOf( TestCase.pop() ) ); 
		System.out.println(TestCase); 
		int sub = Integer.parseInt(Args[0]); 
		System.out.println("PopAt: " + String.valueOf( TestCase.popAt(sub) ) ); 
		System.out.println(TestCase); 
//		System.out.println("Pop: " + String.valueOf( TestCase.pop() ) ); 
//		System.out.println("Pop: " + String.valueOf( TestCase.pop() ) ); 
		//System.out.println("Pop: " + String.valueOf( TestCase.pop() ) ); 
//		System.out.println("Pop: " + String.valueOf( TestCase.pop() ) ); 

		System.out.println("PopAt 0: " + String.valueOf( TestCase.popAt(0) ) ); 
		System.out.println("PopAt 0: " + String.valueOf( TestCase.popAt(0) ) );
		System.out.println(TestCase); 
		System.out.println("Pop: " + String.valueOf( TestCase.pop() ) ); 
//		System.out.println("PopAt 0: " + String.valueOf( TestCase.popAt(0) ) ); 
//		System.out.println("PopAt 0: " + String.valueOf( TestCase.popAt(0) ) ); 
//		System.out.println("PopAt 0: " + String.valueOf( TestCase.popAt(0) ) ); 

		System.out.println(TestCase); 
	}
	/* Run: -ea Plates, ^^ Args: {int} subStack to pop from. */

}

