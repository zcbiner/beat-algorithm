class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def first_common_node(self, list1, list2):
        if list1 is None or list2 is None:
            return None
        
        stack1 = [list1]
        p1 = list1
        loop = 0
        while p1.next is not None:
            p1 = p1.next
            stack1.append(p1)
            loop = loop + 1
        stack2 = [list2]
        p2 = list2
        while p2.next is not None:
            p2 = p2.next
            stack2.append(p2)

        result = None
        while len(stack1) > 0 and len(stack2) > 0:
            temp = stack1.pop()
            if temp is not stack2.pop():
                break
            result = temp
            
        return result



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