# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head #dummy node points to the head
        ptr_dict = {}
        ptr_dict["p"+str(0)] = dummy #points to the dummy node
        for x in range(1, k+1):
            ptr_dict["p"+str(x)] = ptr_dict["p"+str(x-1)].next #points to the next node of the previous node
        
        while True:
            ptr_dict["p"+str(1)].next = ptr_dict["p"+str(k)].next #first pointer now points to the last pointer's next
            for x in range(2, k+1):
                ptr_dict["p"+str(x)].next = ptr_dict["p"+str(x-1)] #nth pointer points to (n-1)th pointer
            ptr_dict["p"+str(0)].next = ptr_dict["p"+str(k)] #dummy pointer points to previous last pointer

            ptr_dict["p"+str(0)] = ptr_dict["p"+str(1)] #dummy pointer is now assigned to first pointer which points to the swapped last node.
            for x in range(1, k+1):
                if ptr_dict["p"+str(x-1)].next != None:
                    ptr_dict["p"+str(x)] = ptr_dict["p"+str(x-1)].next #points to the next node of the previous node
                else:
                    return dummy.next

