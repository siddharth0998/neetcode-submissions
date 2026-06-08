class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack1,stack2 = [p], [q]

        while stack1 and stack2:
            el1 = stack1.pop()
            el2 = stack2.pop()
            if not el1 and not el2:
                continue
            if not el1 or not el2 or el1.val != el2.val:
                return False
            else:
                stack1.append(el1.left)
                stack1.append(el1.right)
                stack2.append(el2.left)
                stack2.append(el2.right)
        if stack1 or stack2:
            return False
        return True