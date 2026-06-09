# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        ind = {val: index for index, val in enumerate(inorder)}
        self.preIndx = 0
        def dfs(l,r):
            if l > r:
                return None
            val = preorder[self.preIndx]
            node = TreeNode(val)
            self.preIndx += 1
            mid = ind[val]
            node.left = dfs(l,mid - 1)
            node.right = dfs(mid + 1,r)
            return node
        return dfs(0,len(preorder)-1)
            