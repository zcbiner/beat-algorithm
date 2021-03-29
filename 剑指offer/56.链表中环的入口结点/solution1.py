class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def entry_of_loop(self, head):
        if head is None:
            return None
        p_slow = head
        p_fast = head
        while p_fast.next is not None and p_fast.next.next is not None:
            p_slow = p_slow.next
            p_fast = p_fast.next.next
            if p_slow is p_fast:
                break
        
        if p_fast is None or p_fast.next is None:
            return None
        
        p_slow = head
        while p_slow is not p_fast:
            p_slow = p_slow.next
            p_fast = p_fast.next
        
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
    node6.next = node4

    result = Solution().entry_of_loop(node1)
    print("%d" %result.data)
