# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # first phase 
        dummy = ListNode(0, head)
        leftPre = dummy
        curr = head

        for i in range(left-1):
            leftPre = curr
            curr = curr.next

        # second phase ... rverese the middle portion
        prev = None
        for i in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # third phase....update pointers
        leftPre.next.next = curr
        leftPre.next = prev
        return dummy.next

        



        