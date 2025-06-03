# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        # Now we get the length
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # now we do calculation if k is bigger than length
        k = k % length
        if k == 0:
            return head

        # now we are going to pivot and join tail in the beginning
        curr = head
        for i in range(length - k -1):
            curr = curr.next # uptil here we are at 3
        newHead = curr.next
        curr.next = None
        tail.next = head
        return newHead

        