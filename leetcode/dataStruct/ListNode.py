class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def buildListNode(num_array):
    dummy = ListNode(0)
    p = dummy
    for item in num_array:
        p.next = ListNode(item)
        p = p.next
    return dummy