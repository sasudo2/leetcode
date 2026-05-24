# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        current = None
        current1 = list1
        current2 = list2
        if current1 == None:
            return current2
        elif current2 == None:
            return current1

        while current1 != None and current2 != None:
            if current1.val > current2.val:
                if head == None:
                    head = current2
                    current = head
                else:
                    current.next = current2
                    current = current2
                current2 = current2.next
            else:
                if head == None:
                    head = current1
                    current = head
                else:
                    current.next = current1
                    current = current.next
                current1 = current1.next
                
        if current1 == None and current2 == None:
            return current
        if current1 == None:
            if current == None:
                current = current2
            else:
                current.next = current2
        else:
            if current == None:
                current = current1
            else:
                current.next = current1
        
        return head