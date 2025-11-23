# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node or node.val == p.val or node.val == q.val:
                return node

            l = dfs(node.left)
            r = dfs(node.right)

            if l and r:
                return node
            if l:
                return l
            else:
                return r
        return dfs(root)