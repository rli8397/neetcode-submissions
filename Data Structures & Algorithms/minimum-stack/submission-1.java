class MinStack {
    private LinkedList<Integer> stack;
    private LinkedList<Integer> min;
    
    public MinStack() {
        min = new LinkedList<Integer>();
        stack = new LinkedList<Integer>();
    }
    
    public void push(int val) {
        if (min.isEmpty() || min.getFirst() >= val) {
            min.addFirst(val);
        }
        stack.addFirst(val);
    }
    
    public void pop() {
        int removed = stack.remove();
        if (removed == min.getFirst()) {
            min.remove();
        }
    }
    
    public int top() {
        return stack.getFirst();
    }
    
    public int getMin() {
        return min.getFirst();
    }
}
