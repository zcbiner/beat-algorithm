package stack;

import java.util.Stack;

/**
 * 仅使用递归逆序一个栈
 */
public class 逆序一个栈 {

    private static int getAndRemoveLastEle(Stack<Integer> stack) {
        int result = stack.pop();
        if (stack.isEmpty()) {
            return result;
        } else {
            int last = getAndRemoveLastEle(stack);
            stack.push(result);
            return last;
        }
    }

    public static void reverse(Stack<Integer> stack) {
        if (stack.isEmpty()) {
            return;
        }
        int i = getAndRemoveLastEle(stack);
        reverse(stack);
        stack.push(i);
    }

    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<>();
        stack.push(0);
        stack.push(1);
        stack.push(2);
        stack.push(3);
        stack.push(4);
        stack.push(5);
        stack.push(6);

        reverse(stack);

        System.out.print("The result after reverse : ");
        for (Integer i : stack) {
            System.out.print(i + " ");
        }
    }
}
