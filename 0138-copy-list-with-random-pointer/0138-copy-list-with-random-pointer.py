"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
       # First create empty hashmap
        oldToCopy = { None : None}

        # Clonning the linkedlist. No pointers are connected yet, just clonning
        curr = head
        while curr:
            # create copy of the node from constructor
            copy = Node(curr.val)
            # Then put it in a hashmap
            oldToCopy[curr] = copy
            curr = curr.next  # update pointer

        # Now connect the pointers to the hashmap
        curr = head
        while curr:
            copy = oldToCopy[curr] # go to the hashmap
            copy.next = oldToCopy[curr.next] # create next pointer
            copy.random = oldToCopy[curr.random] # create random pointer
            curr = curr.next

        # return head of the copy of the linkedlist
        return oldToCopy[head]


        



