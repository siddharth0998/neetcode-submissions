# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = collections.deque([(root,root.val)])
        cnt = 1
        while q:
            node,val = q.popleft()
            if node:
                if node.left:
                    if node.left.val >= val:
                        cnt += 1
                    q.append((node.left,node.left.val if node.left.val > val else val))
                if node.right:
                    if node.right.val >= val:
                        cnt += 1
                    q.append((node.right,node.right.val if node.right.val > val else val))

        return cnt