package list;

/**
 * Created by zhong on 2017/8/3.
 * 单向链表
 */
public class SinglyLinkedList<T> {

    private static class Node<T> {
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
            head = new Node<>(data);
            tail = head;
        } else {
            Node node = new Node(data);
            tail.next = node;
            tail = node;
        }
    }

    // 求单链表中，节点的个数
    public int size() {
        int size = 0;
        Node temp = head;
        while (temp != null) {
            size++;
            temp = temp.next;
        }
        return size;
    }

    // 找单链表中倒数第k个节点
    public Node findLastNode(int k) {
        if (head == null || k < 0) {
            return null;
        }
        Node first = head;
        Node second = head;

        for (int i = 0; i < k - 1; i++) {
            second = second.next;
            if (second == null) {
                return null;
            }
        }

        while (second.next != null) {
            first = first.next;
            second = second.next;
        }
        return first;
    }

    // 找到单链表中间节点
    public Node findMiddleNode() {
        if (head == null) {
            return null;
        }
        Node first = head;
        Node second = head;
        while (second != null && second.next != null) { // 注意这个判断条件
            second = second.next.next;
            first = first.next;
        }
        return first;
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

//    public static Node mergeLinkList(Node h1, Node h2) {
//
//    }
}
