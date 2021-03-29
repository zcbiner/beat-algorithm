class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def first_common_node(self, list1, list2):
        if list1 is None or list2 is None:
            return None
        
        # 获取链表1的长度
        p1 = list1
        list1_count = 1
        while p1.next is not None:
            p1 = p1.next
            list1_count = list1_count + 1
        
        # 获取链表2的长度
        p2 = list2
        list2_count = 1
        while p2.next is not None:
            p2 = p2.next
            list2_count = list2_count +1
        
        # 找到更长的链表并计算差值
        p_ahead = list1
        p_behind = list2
        diff = list1_count - list2_count
        if list1_count < list2_count:
            p_ahead = list2
            p_behind = list1
            diff = list2_count - list1_count
        
        # 长链表先遍历到差值位置
        for i in range(diff):
            p_ahead = p_ahead.next
        
        # 两个链表一起遍历，遇到第一个相同的结点即为结果
        while p_ahead is not p_behind:
            p_ahead = p_ahead.next
            p_behind = p_behind.next
        
        return p_ahead

if __name__ == '__main__':
    list1_node1 = Node(1)
    list1_node2 = Node(2)
    list1_node1.next = list1_node2
    list1_node3 = Node(3)
    list1_node2.next = list1_node3
    list1_node4 = Node(4)
    list1_node3.next = list1_node4
    list1_node5 = Node(5)
    list1_node4.next = list1_node5
    list1_node6 = Node(6)
    list1_node5.next = list1_node6
    list1_node7 = Node(7)
    list1_node6.next = list1_node7

    list2_node1 = Node(10)
    list2_node2 = Node(11)
    list2_node1.next = list2_node2
    # 第一个公共相交点
    list2_node3 = list1_node5
    list2_node2.next = list2_node3
    list2_node4 = list1_node6
    list2_node5 = list1_node7

    result = Solution().first_common_node(list1_node1, list2_node1)
    print("first_common_node is %d" %result.data)