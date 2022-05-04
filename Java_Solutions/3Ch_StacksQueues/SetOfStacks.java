
import java.util.ArrayList; 
import java.lang.IllegalArgumentException; 
import java.util.EmptyStackException; 

/*
 * Represents a stack of plates where: 
 * 	Dynamic array of int arrays Stax holds the piles. 
 * 	Var threshold is how many plates we allow to be stacked before we move the next plate to a new pile. 
 * 	Var currentStacks keeps track of the most recent pile (-1 no pile, 0 first).  
 * 	Var top points to the most recent plate stacked (-1 table or floor [no plate], 0 bottom plate). 
 */

public class SetOfStacks {
	private final ArrayList<int[]> Stax;
	private int threshold; 
	private int currentStack; 
	private int top; 

	public SetOfStacks(int finalThreshold) throws IllegalArgumentException {
		if (finalThreshold < 1) throw new IllegalArgumentException("Threshold must be greater than 0. "); 
		this.threshold = finalThreshold; 
		this.currentStack = -1; 
		this.Stax = new ArrayList<int[]>(); 
		this.top = -1; 
	}

	public boolean isEmpty() {
		return (this.currentStack == -1); 
	}

	/*
	 * If there are no piles or the last pile is already wobbling, start a new pile. 
	 * Place the plate at the top of the most recent pile. 
	 */
	public void push(int newValue) {
		if (this.isEmpty() || this.top == this.threshold-1) this.createNewStack(); 
		( this.Stax.get(currentStack) )[++top] = newValue; 
	}

	/*
	 * If we removed the last plate form a pile, remove that pile. 
	 * Reduces top. 
	 */
	public int pop() throws EmptyStackException {
		if (this.isEmpty() || this.top == -1) throw new EmptyStackException(); 
		int returnValue = ( this.Stax.get(currentStack) )[top--]; 
		if (this.top == -1) this.deleteLastStack(); 
		return returnValue; 
	}

	/*
	 * Assume SetOfStacks will never be empty when calling this method. 
	 * Set var top to top of previous pile or to the table if the first pile was removed. 
	 * Removes last pile and reduces currentStack. 
	 */
	private void deleteLastStack() {
		assert ( !( this.isEmpty() ) ); 
		this.top = (this.currentStack > 0) ? this.threshold - 1 : -1; 
		this.Stax.remove(currentStack--); 
	}

	/*
	 * Set top to table as this new pile has no plates in it yet. 
	 * Add new pile (array of ints of size threshold) to Stax. 
	 * Increments currentStack. 
	 */
	private void createNewStack() {
		this.top = -1; 
		this.currentStack++; 
		this.Stax.add(new int[this.threshold]); 
	}

	// FOLLOW UP: 
	/* 
	 * If index is last stack simply pop. 
	 * If index is not last stack, 
	 * 	return value is always threshold-1. 
	 * 	Move over all elements after it. 
	 */
	public int popAt(int index) throws EmptyStackException, IllegalArgumentException {
		if (this.isEmpty() || this.top == -1) throw new EmptyStackException(); 
		if (index > this.currentStack || index < 0) 
			throw new IllegalArgumentException("Invalid value for index. Substacks (1st index: 0): " + 
					String.valueOf(this.currentStack + 1) + ". " ); 

		if (index == this.currentStack) return ( this.pop() ); 

		int returnValue = ( this.Stax.get(index) )[this.threshold-1]; 

		// Update top. If a stack was not deleted, --: 
		if ( this.moveOver(index) ) top--; 

		return returnValue; 
	}

	/*
	 * Base cases: recursed to last stack OR last stack empty. 
	 * Move bottom element of next stack to TOP element of this stack. 
	 * Move rest of next stack down or delete last stack if no more elements above. 
	 * Recurse to next stack. 
	 * Return true if last stack was NOT deleted. 
	 */
	private boolean moveOver(int index) {
		assert this.top != -1 && !this.isEmpty(); 

		// Base case. Stop when last stack reached:  
		if (index == this.currentStack) return true; 
	
		// Move bottom element of next stack to TOP element of this stack: 
		( this.Stax.get(index) )[this.threshold-1] = ( this.Stax.get(index+1) )[0]; 

		// Delete last stack if no more elements above: 
		if (this.top == 0 && index+1 == this.currentStack) {
			this.deleteLastStack(); 
			return false; 
		}

		// Move rest next stack down:
		// Rise from bottom to (top if next stack is last) OR threshold. 
		int lim = (index+1 == this.currentStack) ? this.top : this.threshold-1; 
		for (int rise = 0; rise < lim; rise++) 
			( this.Stax.get(index+1) )[rise] = ( this.Stax.get(index+1) )[rise+1]; 

		// Recurse. Return to let the false value in case a stack was deleted to bubble up: 
		return moveOver(index+1);  
	}

	// DO NOT REFACTOR. 
	@Override 
	public String toString() {
		String Repr = "{SetOfStacks: "; 
		for (int subStack = 0; subStack <= this.currentStack; subStack++) {
			Repr += "[ "; 
			if (subStack == this.currentStack) {
				for (int sink = 0; sink <= this.top; sink++) {
					Repr += String.valueOf( ( this.Stax.get(subStack) )[sink] ) + " "; 
					if (sink != this.top) Repr += "|"; 
				}
			} else {
				for (int sink = 0; sink < this.threshold; sink++) {
					Repr += String.valueOf( ( this.Stax.get(subStack) )[sink] ) + " "; 
					if (sink != this.threshold-1) Repr += "|"; 
				}
			}
			Repr += "], "; 
		}
		return Repr + "} "; 
	}

}

