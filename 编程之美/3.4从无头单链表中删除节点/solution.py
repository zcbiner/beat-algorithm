class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def del_node(self, p_del):
        # 竟然题目明确说了p_del既不是第一个结点也不是最后一个，就不做合法性校验。
        p_next = p_del.next
        # 替换结点数据
        p_del.data = p_next.data
        # 删除p_next
        p_del.next = p_next.next


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

    Solution().del_node(node3)
    p = node1
    while p is not None:
        print(p.data)
        p = p.next