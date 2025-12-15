class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root):
        # Way to nearest left node
        return self.HeightRoot(root)
    def HeightRoot(self, root):

        lHeight = self.HeightRoot(root.left)
        rHeight = self.HeightRoot(root.right)

        if lHeight == 0:
            return rHeight
        if rHeight == 0:
            return lHeight
        
        return 1 + min(lHeight, rHeight)