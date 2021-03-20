class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 剑指off解法
class Solution:
    # 快慢指针获取相遇结点
    def metting_node(self, head):
        if head is None:
            return None

        p_slow = head.next
        if p_slow is None:
            return None
        
        p_fast = p_slow.next
        while p_fast is not None and p_slow is not None:
            if p_fast is p_slow:
                # 相遇则返回相遇结点
                return p_fast
            p_slow = p_slow.next
            p_fast = p_fast.next
            if p_fast is not None:
                p_fast = p_fast.next
        
        return None
    
    def entry_of_loop(self, head):
        node_metting = self.metting_node(head)
        if node_metting is None:
            return None
        
        p1 = node_metting
        loop_size = 1
        # 获取到环的结点数
        while p1.next is not node_metting:
            p1 = p1.next
            loop_size = loop_size + 1
        
        p1 = head
        for i in range(loop_size):
            p1 = p1.next
        
        p2 = head
        while p1 is not p2:
            p1 = p1.next
            p2 = p2.next
        
        return p1

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
    node6.next = node3

    result = Solution().entry_of_loop(node1)
    print("%d" %result.data)