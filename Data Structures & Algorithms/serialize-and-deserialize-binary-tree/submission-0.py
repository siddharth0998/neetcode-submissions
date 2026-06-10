# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        list = []
        def dfs(root):
            if not root:
                list.append("N")
                return
            list.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(list)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.ind = 0
        vals = data.split(",")
        def dfs():
            if vals[self.ind] == "N":
                self.ind += 1
                return None
            node = TreeNode(vals[self.ind])
            self.ind += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()











