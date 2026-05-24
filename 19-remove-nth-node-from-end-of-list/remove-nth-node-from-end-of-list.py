# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node_dict = {}
        current = head
        index = 0
        # index_list = []
        new_head = None
        while current != None:
            node_dict[index] = current
            index += 1
            current = current.next

        node_dict.pop(index - n)
        # index_list.pop(index - n + 1)
        # new_head = node_dict.pop([index_list.pop(0)])
        for index, node in node_dict.items():
            if new_head == None:
                new_head = node
                current = new_head
                current.next = None
            else:
                current.next = node
                current = node
                current.next = None
        return new_head
