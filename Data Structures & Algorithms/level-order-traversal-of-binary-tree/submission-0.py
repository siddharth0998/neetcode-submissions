# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        list = []
        def dfs(root,list,depth):
            if not root:
                return
            if len(list) == depth:
                list.append([])
            list[depth].append(root.val)
            dfs(root.left,list,depth+1)
            dfs(root.right,list,depth+1)
        dfs(root,list,0)
        return list