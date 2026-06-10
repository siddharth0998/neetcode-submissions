# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max = -10000
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.max = max(self.max,root.val+left+right,root.val,root.val+left,root.val+right)
            return root.val + max(left if left > 0 else 0,right if right > 0 else 0)
        dfs(root)
        return self.max