class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root):
        return self.checkedBalanced(root) >= 0
    def checkedBalanced(self, root):
        if root is None:
            return 0
        
        lHeight = self.checkedBalanced(root.left)
        rHeight = self.checkedBalanced(root.right)

        if abs(lHeight - rHeight) > 1 or lHeight == -1 or rHeight == -1:
            return -1
        return 1 + max(lHeight, rHeight)