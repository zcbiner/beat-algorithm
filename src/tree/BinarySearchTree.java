package tree;

public class BinarySearchTree {
    private Node root;

    private class Node {
        Node left;
        Node right;
        int key;
        Object value;

        public Node(int key, Object value) {
            this.key = key;
            this.value = value;
        }
    }

    public Object get(int key) {
        Object result = null;
        Node node = root;
        while (node != null) {
            if (key == node.key) {
                result = node.value;
                break;
            } else if (key > node.key) {
                node = node.right;
            } else {
                node = node.left;
            }
        }
        return result;
    }

    public void put(int key, Object value) {
        if (root == null) {
            root = new Node(key, value);
        } else {
            putNode(root, key, value);
        }
    }

    private Node putNode(Node x, int key, Object value) {
        if (key > x.key) {
            x.right = putNode(x.right, key, value);
        } else if (key < x.key) {
            x.left = putNode(x.left, key, value);
        } else {
            x.value = value;
        }
        return x;
    }

    public void add(int key, Object value) {
        if (root == null) {
            root = new Node(key, value);
        } else {
            add(root, key, value);
        }
    }

    private void add(Node node, int key, Object value) {
    }

    public Node getMax() {
        Node max = root;
        if (max == null) return null;
        while (max.right != null) {
            max = max.right;
        }
        return max;
    }

    public Node getMin() {
        Node min = root;
        if (min == null) return null;
        while (min.left != null) {
            min = min.left;
        }
        return min;
    }

    public void delete(int key) {
        deleteNode(null, root, key);
    }

    private void deleteNode(Node parent, Node node, int key) {
        if (key > node.key) {
            deleteNode(node, node.right, key);
        } else if (key < node.key) {
            deleteNode(node, node.left, key);
        } else {
            if (node.left == null && node.right == null) {
                if (parent.left == node) {
                    parent.left = null;
                } else {
                    parent.right = null;
                }
            } else if (node.left != null && node.right != null) {
                Node min = node.right;
                while (min.left != null) {
                    min = min.left;
                }
                node.key = min.key;
                node.value = min.value;
                min = null;
            } else {
                if (parent.left == node) {
                    parent.left = node.left == null ? node.right : node.left;
                } else {
                    parent.right = node.left == null ? node.right : node.left;
                }
            }
        }
    }

    public void preTree() {
        preTree(root);
    }

    private void preTree(Node node) {
        if (node == null) return;
        System.out.print(node.value + " ");
        preTree(node.left);
        preTree(node.right);
    }

    public void inTree() {
        inTree(root);
    }

    private void inTree(Node node) {
        if (node == null) return;
        inTree(node.left);
        System.out.print(node.value + " ");
        inTree(node.right);
    }

    public void afTree() {
        afTree(root);
    }

    private void afTree(Node node) {
        if (node == null) return;
        afTree(node.left);
        afTree(node.right);
        System.out.print(node.value + " ");
    }

    public static void main(String[] args) {
        BinarySearchTree tree = new BinarySearchTree();
        tree.put(2, "2");
        tree.put(6, "6");
        tree.put(9, "9");
        tree.put(1, "1");
        tree.put(5, "5");
        tree.put(8, "8");
        tree.put(10, "10");
        tree.put(0, "0");
        tree.put(12, "12");
        tree.put(13, "13");
        tree.put(3, "3");
        tree.put(11, "11");

        tree.delete(9);
        tree.preTree();
        System.out.println();
        tree.inTree();
        System.out.println();
        tree.afTree();
    }
}
