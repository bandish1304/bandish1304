"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return root
        q = [root]
      
        while q:
            n = len(q)
            prev = None
            for i in range(n):
                curr = q[i]
                if prev:
                    prev.next = curr
                prev = curr
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            
            q = q[n:]
        return root


        