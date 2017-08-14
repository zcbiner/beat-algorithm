package list;

/**
 * Created by zhong on 2017/8/4.
 * 双向链表
 */
public class MLinkedList<T> {
    private int size = 0;
    private Node head;
    private Node tail;

    public void add(T data) {
        if (head == null) {
            head = tail = new Node(data, null, null);
            size++;
        } else {
            Node node = new Node(data, tail, null);
            tail.next = node;
            tail = node;
            size++;
        }
    }

    public boolean remove(T data) {
        if (head == null) {
            return false;
        }
        Node temp = head;
        while (temp.next != null) {
            if (temp.data.equals(data)) {
                temp.pre.next = temp.next;
                temp.next.pre = temp.pre;
                size--;
                return true;
            }
        }
        return false;
    }

    private class Node {
        T data;
        Node pre;
        Node next;

        public Node(T data, Node pre, Node next) {
            this.data = data;
            this.pre = pre;
            this.next = next;
        }
    }
}
