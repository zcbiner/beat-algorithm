package stack;

import java.util.Stack;

public class getMin功能的栈 {

    private Stack<Integer> stack = new Stack<>();
    private Stack<Integer> minStack = new Stack<>();

    public int pop() {
        int value = stack.pop();
        if (value == minStack.peek()) {
            minStack.pop();
        }
        return value;
    }

    public void push(int value) {
        stack.push(value);
        if (minStack.empty()) {
            minStack.push(value);
        } else if (value <= minStack.peek()) {
            minStack.push(value);
        }
    }

    public int getMin() {
        return minStack.peek();
    }
}
