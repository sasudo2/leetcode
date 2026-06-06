# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        top = None
        temp = None
        a = head
        if head == None or head.next == None:
            return head
        b = head.next
        while b != None and a != None:
            if top == None:
                top = ListNode(b.val)
                temp = top
                temp.next = ListNode(a.val)
                temp = temp.next
                a = a.next.next
                if b.next == None:
                    break
                b = b.next.next
            else:
                temp.next = ListNode(b.val)
                temp = temp.next
                temp.next = ListNode(a.val)
                temp = temp.next
                a = a.next.next
                if b.next == None:
                    break
                b = b.next.next
        if a != None:
            temp.next = ListNode(a.val)
            temp = temp.next
        return top
