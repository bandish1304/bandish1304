# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        #Bring right pointer to n , so we have to loop
        while n > 0 and right:
            right = right.next
            n = n-1

        # Now shift both the pointer till right goes out of bound
        while right:
            right = right.next
            left = left.next

        # join the left pointer to the next node
        left.next = left.next.next
        return dummy.next
