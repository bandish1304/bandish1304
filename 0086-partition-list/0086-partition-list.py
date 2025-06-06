# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # split into two. Left and right
        left = ListNode()
        right = ListNode()
        leftTail = left
        rightTail = right

        while head:
            if head.val < x:
                leftTail.next = head
                leftTail = leftTail.next
            else:
                rightTail.next = head
                rightTail = rightTail.next
            head = head.next
         
        # Now we connect both left and right
        leftTail.next = right.next
        rightTail.next = None
        return left.next



        