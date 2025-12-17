from typing import Optional
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 +  self.countNodes(root.left) + self.countNodes(root.right)
    
class Solution2:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        left_h, right_h = self.getHeightsL(root), self.getHeightsR(root)

        if left_h == right_h:
            # Bitwise manipulation, * 2 and - 1
            return (1 << left_h) - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def getHeightsL(self, root):
        height = 0
        while root:
            height += 1
            root = root.left

        return height
    
    def getHeightsR(self, root):
        height = 0
        while root:
            height += 1
            root = root.right

        return height