# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        elements = []
        for link_list in lists:
            current = link_list
            while current != None:
                elements.append(current.val)
                current = current.next

        elements.sort()
        head = None
        current = None
        for element in elements:
            if head == None:
                head = ListNode(element)
                current = head
            else:
                current.next = ListNode(element)
                current = current.next
        
        return head