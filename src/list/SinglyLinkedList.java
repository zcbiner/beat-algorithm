package list;

/**
 * Created by zhong on 2017/8/3.
 * 单向链表
 */
public class SinglyLinkedList<T> {

    private class Node {
        private T data;
        private Node next;

        Node(T data) {
            this.data = data;
        }
    }

    private Node head;
    private Node tail;

    public void add(T data) {
        if (head == null) {
            head = new Node(data);
            tail = head;
        } else {
            Node node = new Node(data);
            tail.next = node;
            tail = node;
        }
    }

    public boolean remove(T data) {
        if (head == null) {
            throw new IndexOutOfBoundsException("SinglyLinkedList is null");
        } else {
            Node temp = head;
            if (temp.data.equals(data)) {
                head = temp.next;
                temp = null;
                return true;
            } else {
                while (temp.next != null) {
                    Node pre = temp;
                    temp = temp.next;
                    if (temp.data.equals(data)) {
                        pre.next = temp.next;
                        temp = null;
                        return true;
                    }
                }
                return false;
            }
        }
    }

    public void addToHead(T data) {
        if (head == null) {
            head = new Node(data);
        } else {
            Node node = new Node(data);
            node.next = head;
            head = node;
        }
    }

    public boolean contains(T data) {
        if (head == null) {
            return false;
        } else {
            if (head.data.equals(data)) {
                return true;
            } else {
                Node temp = head;
                while (temp.next != null) {
                    temp = temp.next;
                    if (temp.data.equals(data)) {
                        return true;
                    }
                }
                return false;
            }
        }
    }

    public void printThis() {
        if (head == null) {
            return;
        }

        Node temp = head;
        while (temp.next != null) {
            System.out.println(temp.data.toString());
            temp = temp.next;
        }
        System.out.println(temp.data.toString());
    }

    /**
     * 反转链表
     */
    public void reverse() {
        if (head == null) {
            return;
        }

        Node pre = head;
        while (head != null) {
            Node next = head.next;
            head.next = pre;
            pre = head;
            head = next;
        }

    }
}
