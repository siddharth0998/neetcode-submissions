# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = None
        stack = [root]
        while stack:
            node = stack.pop()
            if (node.val >= p.val and node.val <= q.val) or (node.val >= q.val and node.val <= p.val):
                res = node
                break
            else:
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
        return res

        
        
        
