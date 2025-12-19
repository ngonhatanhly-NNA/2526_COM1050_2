from typing import Optional, List
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return
        
        curr = root
        # Youh can see it go in this pattern, right most linked to the right tree
        # and the next right most linked to the one before
        while curr:
            if curr.left:
                last = curr.left
                while curr.right:
                    last = last.right
                
                last.right = curr.right
                curr.right = curr.left
                curr.left = None

            curr = curr.right
        
                
