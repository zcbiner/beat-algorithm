class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def k_for_last(self, node_head, k):
        p_fast = node_head
        p_slow = node_head
        for i in range(1, k):
            if p_fast.next is None:
                return None
            p_fast = p_fast.next

        while p_fast.next is not None:
            p_fast = p_fast.next
            p_slow = p_slow.next
        
        return p_slow


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    solution = Solution()
    result = solution.k_for_last(node1, 4)
    print("%d" %result.data)